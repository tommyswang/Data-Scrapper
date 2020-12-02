# Research and Experiments Report #

**Team Name:** HZ-TASK Force

**Team Members:** Allen Leigh, Hongyu Cheng, Kanishkah Anwari, SeGe Jung, Tommy Wang, Zahiduzzaman Biswas

**Project Name:** Data Scraper

**GitHub Link:** https://github.gatech.edu/gt-cs6440-hit-fall2020/Data-Scrapper

In recent years, electronic health data is collected and stored via pdf files, digital forms, remote database, cloud platforms and Internet of Things. As a result, the medical data are extracted and ingested in different format. Researchers have developed standards like HL7 to keep consistency in the data collection formats. Yet many tools have not achieved that standard yet. 

In our research, we have found that organizations like CDC, State health departments, as well as many research institutes are still using multiple tools to extract and store all the new data. A significant amount of effort is in progress to develop an all-purpose solution for the data mining. AWS, Palantir, Google cloud, azure and many other companies have created a platform with combination of many tools to serve that purpose. However, the main issue of cost remains. 

There are several open sources as well as premium tools are available in the market for extracting data from HTML and API sources. These tools are primarily built on the popular programming languages like JAVA, Python, SaaS and so on. The standard libraries used in these tools are also available for open source developments. While premium services guarantee security and certain standard of data, in terms accuracy open source solutions are also quite reliable. 

Since most of the data in the clinical research and hospitals are collected by filling forms, extraction of data from different type of files are a topic of continuous research and development. Specially, extracting data from pdf files, while maintaining 100% accuracy, is yet to be introduced. 

Open sources libraries can extract tabular data quite easily, but the form data lacks accuracy. Even when the tabular data is not properly formatted or the format is not well defined in the backing encoding, most of these libraries fails the task. Tabula and Camelot are two popular python library that can extract tabular data from almost all types of pdf encoding.
However, there is a need of reliable tool when it comes to parsing pdf forms. In an interview with Grishma, an Epidemiologist from CDC, told us that in the mycotic lab, researchers are still ingesting data manually in a data mining tool called Foundry, developed by Palantir technology. Another Epidemiologist, Andrea Mansur, said they are moving their data to AWS. They are also using Foundry, but it is integrated with AWS. However, it requires them to have a monthly subscription to extract and store data, which cost them a big number. 

Some of the popular open source libraries in python language promise to extract data from acroform and xml based pdf forms. Pdfminer, and pdfplumber were two of the libraries that were able to decode all types of pdf documents regardless of which tools it is created from. Pypdf failed to extract 128 bit encoded pdfs. Slate, pdfquery and other libraries can serialize the annotations to extract data and text only. However, they cannot relate the data with corresponding fields. These libraries cannot extract the checkbox and radio responses either. A list of the research results and documents are added to the corresponding directory for references. 
