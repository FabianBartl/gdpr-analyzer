
import json
import sys
import subprocess
import filedate
import numpy as np
import dateutil.parser
from PIL import Image
from pathlib import Path
from tqdm import tqdm
from typing import Union



# removes the user id from the path, removes leading '/'
def fix_path(path: Union[Path, str], userid: str) -> Path:
    new_path = str(path).replace(f"/{userid}/", "/")
    if new_path.startswith("/"):
        new_path = new_path[1:]
    return Path(new_path)


def process_memories(data_package: Path) -> None:
    global EXIFTOOL_BIN, EMBED_LOCATION
    
    # read memories json
    with open(data_package / "memories.json", "r", encoding="utf-8", errors="replace") as fobj:
        data_memories = json.load(fobj)

    # extract userid from path
    userid = data_memories[0]["frontImage"]["path"].split("/")[2]

    # parse memories
    memories = []
    for data_memory in tqdm(data_memories, desc="parse memories"):
        memory = {
            "frontImage": data_package / fix_path(data_memory["frontImage"]["path"], userid),
            "backImage": data_package / fix_path(data_memory["backImage"]["path"], userid),
            "caption": data_memory.get("caption", None),
            "isLate": data_memory["isLate"],
            "date": dateutil.parser.isoparse(data_memory["date"]),
            "takenTime": dateutil.parser.isoparse(data_memory["takenTime"]),
            "berealMoment": dateutil.parser.isoparse(data_memory["berealMoment"]),
            "location": data_memory.get("location", None),
        }
        memories.append(memory)
    memories.sort(key=lambda m: m["takenTime"])
    
    # create export directory for memories    
    export_directory = data_package / "export" / "memories"
    export_directory.mkdir(parents=True, exist_ok=True)
    
    # create combined images
    memory_errors = []
    name_memory_mapping = {}
    for memory in tqdm(memories, desc="combine images"):
        try:
            front_image = Image.open(memory["frontImage"])
            back_image = Image.open(memory["backImage"])
            
            # stack horizontally
            collage_image = Image.new("RGB", (front_image.width+back_image.width, front_image.width))
            collage_image.paste(front_image, (0, 0))
            collage_image.paste(back_image, (front_image.width, 0))
        
            # create filename, map the memory entry to it and store as jpg
            filename = Path(memory["takenTime"].strftime("%Y-%m-%d %H-%M-%S") + "_bereal.jpg")
            collage_image.save(export_directory / filename)
            name_memory_mapping[filename] = memory
        
        except Exception as exc:
            print(memory["frontImage"], exc)
            memory_errors.append(memory)
    print("errors:", memory_errors)

    # edit metadata
    for name, memory in tqdm(name_memory_mapping.items(), desc="write metadata"):
        # embed location into EXIF data of the image file
        if EMBED_LOCATION and memory["location"]:
            lat = memory["location"]["latitude"]
            lon = memory["location"]["longitude"]
            process = subprocess.check_output([EXIFTOOL_BIN, "-overwrite_original", f"-GPSLatitude*={lat}", f"-GPSLongitude*={lon}", str(export_directory / name)])

        # set all file dates to taken time
        taken_time = memory["takenTime"]
        exported_file = filedate.File(export_directory / name)
        exported_file.created = taken_time
        exported_file.modified = taken_time
        exported_file.accessed = taken_time
    


if __name__ == "__main__":
    print("script to process a bereal data package")
    
    # check exiftool dependency
    EXIFTOOL_BIN: str = r"exiftool"
    EMBED_LOCATION = True

    try:
        subprocess.check_output([EXIFTOOL_BIN, "-ver"])
    except FileNotFoundError as exc:
        print("exiftool not found, needed for location embedding")
        print("you can download it here: https://www.exiftool.org/")
        print("if it is already installed, please provide the correct path or alias in the script variable EXIFTOOL_BIN")
        
        EMBED_LOCATION = False
        awnser = input("do you want to proceed without exiftool? [y|N] ").lower()
        if awnser != "y":
            exit()

    # get package path
    for ind, arg in enumerate(sys.argv):
        if ind == 1:
            data_package = Path(sys.argv[ind])
    
    # process data
    print("combine front and back images, set file creation time to the taken time and embedd location data")
    process_memories(data_package)
