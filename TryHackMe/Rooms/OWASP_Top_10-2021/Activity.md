# Activity performed as part of OWASP Top 10 - 2021

- **Pre-requisite** :
1. Start the attack box and the target machine provided.

- **Broken Access Control (IDOR Challenge)** :
1. Visit the target on the browser. Login using the credentials provided.
2. As we are able to view the endpoint: http://<TargetIP>/note.php?note_id=1 used to access notes made by a user.
3. Lets try to check if we are able to access different nodes that are not made by the logged in user.
4. To get the flag read through the notes and figure out the clue as to which note_id has the flag. Hint: What is Aryabhatta's contribution in the field of Mathematics(Number system).

- **Cryptographic Failures (Challenge)**:
1. Visit the target on the browser. 
2. Navigate to Login page and inspect the source to find the endpoint used to access the database.
3. Navigate to the endpoint found, download the flatfile on to your local machine using the wget command. command:"wget <File_link>".
4. Using sqlite3 access the contents of the flatfile.
5. command:"sqlite3 <File>" This command enables user to access the flat file using the sql queries.
6. sql-lite query:".tables" This query retrives all  the tables that are part of the flatfile.
7. sql-lite query:"PRAGMA table_info(<Table_name>)" This query is used to get the table information of mentioned table in query.
8. sql-lite query:"SELECT * FROM <Table_name>" This query is used to get all the contents of the table.
9. Get the admin password hash and crack it using the crackstation online tool. Using the password login to the application and get the flag.

- **3.1. Command Injection** :
1. Navigate to the target web-app provided.
2. Command:"$(ls -l)". When the command is passed as text into the textbox of the application as we are aware of the application design the command injection takes place and we get the desired result.
2. Command:"$(cut -d: -f1 /etc/passwd)". The command lists the list of all user available on the system. -d specifies the delimiter ':'. -f specifies the field that user wants to extract.
3. Command:"$(whoami)". display the username of the current effective user ID (EUID) operating the shell or script.
4. Command:"$(cat /etc/passwd | grep "apache")". Provide the extarcted result of user apache from the cat result of /etc/passwd.
5. Command:"$(cat /etc/alpine-release)". To get the version of Alpine running.

- **4. Insecure Design** :
1. To understand the design flaw of the application provided as target user must go through did scenarios to access joseph's account.
2. One design flaw that was identfied was that the security question can be selected and answered multiple times.
3. Among the questions there is question about favorite color which can be guessed upon repeated. Start with basic color guess and move on.
4. Upon landing on valid color, user gets the reset password. 
5. Login using the new password and navigate through files and get the flag.

- **5. Security Misconfiguration** :
1. Navigate to the target provided.
2. Navigate to /console endpoint of the target.
3. In order get the list of files available on the server side. User can use the python code: "import os; print(os.popen("ls -l").read())"
4. As the result of prsvious code execution user should be able to view list of all the files available on server side.
5. In order to look through the source code of the application and futher get a foothold and use data present on db. use the python code:"import os; print(os.popen("cat app.py").read()).
Note: This is the security misconfiguration on the target. Directory listing is not disabled on the server. An attacker discovers they can simply list directories.

- **Vulnerable and Outdated Components - Lab** :
1. Although found that the application vulnerable to SQLi it was not neccessarily helpful finding information needed.
2. Additional found that basic guessable passwords are working.
3. Utilizing the hint landed on to exploit DB: https://www.exploit-db.com/exploits/47887.
4. Using the script, Exploit and get the RCE shell. Use command: "python3 <script_name> <Target>".
5. Use few basic command first to validate the exploitation like whoami, ls etc.
6. Use the command:"cat <file_location>". To get the flag.

- **Identification and Authentication Failures Practical** :
1. Navigate to Target provided.
2. Navigate to Register page of the target web application.
3. Exploit the authentication login, re-register existing users with additional space preceeding the name as username. Provide other details and register.
4. Use the newly registered user credentials to login to access existing user.

- **Software Integrity Failures** :
1. Visit "https://www.srihash.org/". 
2. Provide "url:https://code.jquery.com/jquery-1.12.4.min.js" as input to the tool. 
3. Change the algorithm which you need and click on Hash.

- **Data Integrity Failures** :
1. Navigate to the target provided and login using username: guest, password: guest. 
2. Checkout the session cookie available in the storage. 
3. Copy the whole session cookie value and extract header and payload part of the cookie. 
4. Decode using the online tool: https://appdevtools.com/base64-encoder-decoder.
5. Modify the alg parameter of the header json to "none" and username parameter of the payload json to "admin". 
6. Encode both header and payload separately and construct a cookie with structure:"<Header>.<Payload>."
7. Enter this value to the session cookie and refresh the screen to get the required flag as admin.

- **9. Security Logging and Monitoring Failures** :
1. Download the analysis log file. 
2. Look through the logs availiable on the file.
3. What looks sus to you once looking through. There are few login which result in un-authorized response.
4. As a single user trying brute force way through to the system using possible user credentials.

- **10. Server-Side Request Forgery (SSRF)** :
1. Navigate to target, Look through the application to get an understanding on the application.
2. Navigate to Admin Area. 
3. Checkout the source code available for Download resume and get the server name.
4. Change the server to the attack box/personal pc. Click on the Download Resume button.
5. Before step 4 use the command:"nc -lvnp <port>", run the netact server.
6. EXTRA CREDIT: As we know "server" is path parameter. Change it to "http://localhost:<port>/admin%23". To get the access to admin area.



