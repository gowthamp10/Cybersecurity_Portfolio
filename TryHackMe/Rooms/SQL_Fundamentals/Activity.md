# Activity performed as part of SQL Fundamentals

- **Pre-requisite** :
1. Run the VM prrovided for practicing.

- **SQL** :
1. Setting up MySQL command: "mysql -u root -p". Provide the password as tryhackme once prompted to.

- **Database and Table Statements** :
1. Once logged to mysql terminal. Use "SHOW DATABASES;" command to get the list of all the databases present, which additionally includes flag need.
2. According to the question we need to use the task_4_db database. Use the command:"USE <db_name>". Then use the command:"SHOW TABLES", which provides the tables present in the db.

- **CRUD Operations** :
1. Use the tools_db database using the command:"USE <db_name>;".
2. Use SELECT statement to retrive data from the hacking_tools table. command:"SELECT * FROM <table_name>;".
3. Based on the data answer the question.

- **Clause** : Pre-requisite is to use the database specified in the question.
1. Total number of distinct categories in the hacking_tools table. Use the SQL query: "SELECT DISTINCT category FROM hacking_tools";
2. First tool (by name) in ascending order from the hacking_tools table. Use the SQL query:"SELECT * FROM hacking_tools ORDER BY name ASC";
3. First tool (by name) in descending order from the hacking_tools table. Use the SQL query:"SELECT * FROM hacking_tools ORDER BY name DESC";

- **Operators** :
1. Tool falls under the Multi-tool category and is useful for pentesters and geeks. Use the SQL query:"SELECT * FROM hacking_tools WHERE category = 'Multi-tool' AND description LIKE '%pentesters and geeks%';"
2. Category of tools with an amount greater than or equal to 300. Use the SQL query:"SELECT * FROM hacking_tools WHERE amount >= 300;"
3. Tool falls under the Network intelligence category with an amount less than 100. Use the SQL query:"SELECT * FROM hacking_tools WHERE category = 'Network intelligence' AND 
amount < 100;"

- **Functions** :
1. Tool with the longest name based on character length. Use the SQL query:"SELECT * FROM hacking_tools ORDER BY LENGTH(name) DESC;"
2. The total sum of all tools. Use the SQL query:"SELECT SUM(amount) AS SUM_TOOLS FROM hacking_tools;"
3. The tool names where the amount does not end in 0, and group the tool names concatenated by " & ". Use SQL query:"SELECT GROUP_CONCAT(name SEPARATOR " & ") AS NAME FROM hacking_tools WHERE NOT amount LIKE '%0';"

