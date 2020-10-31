# Project Plan

**Author**: HZ-TASK Force

## 1 Introduction

Project assigned to HZ-TASK Force is Data Scrapper. 
Many public health entities utiize various formats such as PDFs, Websites, Excel, etc for data handling. This causes a lot of inefficiencies and complexity. The goal of this project is to build a tool that will enable easier data hangling for researchers and develepors. PDF, HTML, Form, and API data will output to CSV. The tool should have the ability to save csv files in the tool database. 

## 2 Process Description

The project process is composed of 8 team sprints. The following is each process description. 
------------------
- Activity name: *Project Kick-off (TS#1)*
- Activity description: *Project is kicked-off in this activity. Team is formed and top 10 project list is chosen by the team. The class TAs assign teams a project they will be working on. Once the team and project is decided, project mentor and stakeholders are introduced. Project is introduced briefly by the mentor and a broad idea of what the team will be working on.*
- Entrance criteria: *For this activity, team needs to be formed and project assigned. Also need a project mentor assigned to the team as well.*
- Exit criteria: *To accomplish this activity done, team is formed and project is assigned.*
------------------
- Activity name: *Requirement/Research (TS#2)*
- Activity description: *This activity is the requirement and research phase. The goal is to research about the assigned project. Research use cases, markets, competition, and so on. Study the tool's functionality and limits. The second part is to create more definition to the project scope and requirements. What is the team trying to accomplish for this project? What is the final deliverable? What are we not doing?*
- Entrance criteria: *Need input from GTRI, Tia, Ellie, and Nate on the requirements.*
- Exit criteria: *Clear list of objectives and deliverables laid out. Requirements are finalized and aligned with the stakeholders*
------------------
- Activity name: *Design (TS#3)*
- Activity description: *This activity is wireframing the front end and drafting architecture diagram, which will include tools and languages the team will use. Deployment pipeline for the tool is also laid out. Documentation is updated. Lastly, gantt chart is generated.*
- Entrance criteria: *The team will use the requirements for this project to work on the design.*
- Exit criteria: *To exit, the design needs to be reviewed by the stakeholders and their feedback should be reflected to our design.*
------------------
- Activity name: *Environment Setup (TS#4)*
- Activity description: *For this activity, the goal is to deploy the web tool Hello World app to HDAP. The web tool will be set up using Flask web framework and deployed using Docker to HDAP. The team will also start initial research for parser libraries. All studies are documented in the team folder. Front end wireframe is revised based on the feedback from TS#3.*
- Entrance criteria: *Refer to the architecture diagram to launch our Hello World app. Need to gather sample API, HTML, FORM, and PDF data.*
- Exit criteria: *App is deployed through the pipeline to HDAP.*
------------------
- Activity name: *Front End Implementation & Coding (TS#5)*
- Activity description: *For this activity, the goal is to set up the boiler plate for Flask app, set up pytest unit tests, and deploy the front end to HDAP. Kanban is used to create task list and track progress, which will allow easy delegation of work. Controllers are added and database container is set up in HDAP. The team will continue with the research on parsers and how to optimize them in the team's tool.*
- Entrance criteria: *Refer to the TS#4 feedback.*
- Exit criteria: *Front end is deployed through the pipeline to HDAP.*
------------------
- Activity name: *Baseline Implementation & Coding (TS#6)*
- Activity description: *This activity is the second part of the implementation and coding. Now that there is front end, parser libraries will be added for HTML, FORM, API, and PDF. The goal for this activity is to deploy baseline coding to HDAP. The tool will be able to parse four input type and output URL to download csv file.*
- Entrance criteria: *Refer to the TS#5 feedback.*
- Exit criteria: *Baseline is deployed through the pipeline to HDAP. Tool should be able to take input data, parse, and output csv file by URL*
------------------
- Activity name: *Optimization Implementation & Coding (TS#7)*
- Activity description: *This activity will be an optimization phase from the baseline. The parsing performance will be optimized and will result more accurate results. The front end will also be improved. At the end of this sprint, the app will be deployed to HDAP and pass all pytest.*
- Entrance criteria: *Refer to the TS#6 feedback.*
- Exit criteria: *Optimization is deployed through the pipeline to HDAP. Tool should be able to take input data, parse, and output csv file by URL*
------------------
- Activity name: *Final Implementation & Coding (TS#8)*
- Activity description: *This activity is the final phase. It will reflect feedback from stakeholders and focus heavily on documentation and user manual.*
- Entrance criteria: *Refer to the TS#7 feedback.*
- Exit criteria: *Documentation and revisions based on stakeholder feedback.*

## 3 Team

| Name | Role | Responsiblity |
| ------ | ------ | ------ | 
| SeGe Jung | Project Manager | responsible for understanding the project requirements and aligning the team to work efficienty towards project deliverables. Also responsible for creating project plan, roadmap, and resource allocation. |
| Allen Leigh | Developer | Leading the sprint as master |
| Zahiduzzaman Biswas | Developer | Coming up with architectural diagram and a main developer |
| Tommy Wang | QA | Responsible for deployment pipeline |
| Hongyu Cheng | Developer | Responsible for PDF input type |
| Kanishkah Anwari | Developer/Project Manager | Responsible for front end |
