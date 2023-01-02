# Sistema de Análise TCB
## 🎆 System working
![gif_Tcb](https://user-images.githubusercontent.com/91624923/210192009-21030671-486b-4751-9973-fb4ff7828746.gif)

## ⚙ Functionalities
- ✅ Streamline search processes
- ✅ Assist data analysis processes
- ✅ Deliver an interaction between analysts and databases with greater simplicity
- ✅ Make the process more accurate

## 🛠 Technologies and Tools Used
- ✅ Python (Pandas, psycopg2)
- ✅ PyQT5
- ✅ Postgres

## ⚠️ Necessary Preparations -> Database system and database preparations can be accessed in the **"How to configure Postgres"** file in that same repository. ⚠️

## 🖥️ System Commands and Functions
### Screen 1
![image](https://user-images.githubusercontent.com/91624923/210127600-d50e66a9-2747-4860-896c-e90b980dc580.png)
**Subtitle**

- 1 - Moves the left sidebar, hiding and showing it
- 2 - Minimize Application
- 3 - Compress Application
- 4 - Expand Application
- 5 - Close Application
- 6 - Access Screen 2
- 7 - Access Screen 3

### Screen 2
![image](https://user-images.githubusercontent.com/91624923/210127631-92353eed-af9e-430e-8172-8d094cce953c.png)
**Subtitle**

- 1 - Database to be searched for data
- 2 - Data search table
- 3 - Filter for detailed searches
- 4 - Run the search
- 5 - Resizes the data inside the table for a better visualization
- 6 - Table showing survey data
- 7 - Download the search performed to an excel spreadsheet

**Comands**
- We can perform searches in databases and tables
- With the Filter (item 3) we can include conditional commands in SQL to direct our searches. Commands like “AND”, “OR”, “=”, “!=”, “<”, “>” and others.
- With the Download (item 7) we can run a search and obtain the entire result in an excel spreadsheet (xlsx) with a click. This command will only run when there is a search performed, if there is no search data before generating the file it will condition an error.

### Screen 3
![image](https://user-images.githubusercontent.com/91624923/210127657-57a3ad5e-d711-4f63-a457-198bf284b267.png)
**Subtitle**

- 1 - Environment for the detailed search
- 2 - Data to be searched for in databases and tables
- 3 - Run the search
- 4 - Location where the search response will be presented (Bringing the name of the banks and tables that have the searched reference)

**Comands**
- The system will go through all the databases and tables in the chosen environment looking for the information typed in the search field (item 2). When the search is finished, the system will inform which databases and tables have that information.
- The excel file will be generated in the project folder with the name “`**Tcb_Download_View.xlsx**`"

##Logs
- System logs will be inserted into a file called “loggs_id.log”, which will record all actions performed within the system.
![image](https://user-images.githubusercontent.com/91624923/210127778-9e2ff757-2302-4488-a17c-ead95759da84.png)

