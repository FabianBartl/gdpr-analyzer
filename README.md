
# GDPR Analyzer

A collection of scripts to analyze the data packages containing your personal data stored by different companies. Under [European GDPR law](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en), you have the right to request a copy of any personal data a company stores about you.

Some scripts focus on visualizing collected data, especially usage statistics. For example, Discord records a precise clickstream, which can be analyzed. One implemented feature is generating a graph to show whom you have interacted with the most based on message volume. The emphasis is primarily on data visualizations.
In contrast, BeReal does not collect unnecessary data, such as telemetry. However, a tool is implemented that embeds metadata like GPS location and capture time into the images.


## How can I request my data?

Under [European GDPR law](https://commission.europa.eu/law/law-topic/data-protection/information-individuals_en), you have the right to request a copy of any personal data a company stores about you. This request is often referred to as a "data subject access request" (DSAR).

>Please note that I am not a lawyer, and this is general guidance based on the law.

Here's how you can typically request your data:

1. **Identify the company**: Determine which company you want to request data from. This could be a social media platform, an online service, or any other company that processes your personal data.

2. **Check the privacy policy**: Most companies have a privacy policy that explains how they handle data access requests. Look for a section on data rights or GDPR requests, which may provide specific instructions on how to proceed.

3. **Submit the request**: 
   - **Email**: Companies usually provide an email address for data requests (e.g., privacy@company.com or dpo@company.com). Write a clear email requesting a copy of the data they store about you. Be sure to mention that you are making the request under GDPR rights.
   - **Online forms**: Some companies provide a dedicated form on their website to submit a data access request. You may need to log into your account before submitting the form.

4. **Include necessary details**: Be specific about the data you want to access. In some cases, you may be asked to verify your identity to ensure the request is legitimate. You can provide additional details, such as your account name, email address, and any other relevant identifiers, to help the company locate your data.

5. **Response time**: By law, companies **must** respond to your request within one month. If the request is complex or numerous, they may extend the deadline by an additional two months, but they must inform you within the first month.

6. **Receiving your data**: The company is required to provide the requested data in a commonly used format, such as JSON or CSV. In some cases, they may provide the data directly on their platform for you to download.

7. **Refusal or issues**: If your request is refused or you don’t receive the data within the required timeframe, you have the right to file a complaint with the data protection authority in your country.

Under EU law, companies are **obligated** to comply with these requests. If they fail to do so, they can face very high fines — up to 4% of their annual global turnover or €20 million, whichever is higher.


For every supported data package, there will be a short extension to the 'how to' guide, tailored for the specific company.


For most requests I usally write the following according to german law:
```
Betreff: Datenauskunft nach DSGVO

hiermit fordere ich gemäß Art. 15 DSGVO eine Auskunft über die zu meinem <DIENST> Account gespeicherten personenbezogenen Daten an. Bitte senden Sie mir eine Kopie aller gespeicherten Daten sowie Informationen zur Verarbeitung, Speicherung und Weitergabe meiner Daten.
Meine mit dem Account verknüpfte E-Mail-Adresse lautet: <DEINE EMAIL ODER ANDERE KONTOINFORMATIONEN, UM DICH ZU IDENTIFIZIEREN>
Bitte bestätigen Sie den Eingang dieser Anfrage und teilen Sie mir mit, wann ich mit einer Antwort rechnen kann.
```

It has always worked for me in german, but if you want to be sure, you should write in english:
```
Subject: Data disclosure according to GDPR

I hereby request information about the personal data stored in my <SERVICE> account in accordance with the EU GDPR. Please send me a copy of all stored data, as well as information regarding the processing, storage, and sharing of my data.
My email address associated with the account is: <YOUR EMAIL OR OTHER ACCOUNT INFORMATION TO IDENTIFY YOU>
Please confirm receipt of this request and inform me when I can expect a reply.
```


## Supported data packages

For each data package, there is a folder containing the tools and possibly an example data package (manually created for testing, not real data due to privacy concerns), along with an explanation of the data formats used and their content.

Anyone is welcome to contribute their own scripts by creating an issue or a pull request.

- [x] BeReal
- [x] Discord (see [@InformaticFreak/discord-data-analyzer](https://github.com/InformaticFreak/discord-data-analyzer))
- [ ] Netflix
- [ ] Pokémon-Go
- [ ] OpenAI


