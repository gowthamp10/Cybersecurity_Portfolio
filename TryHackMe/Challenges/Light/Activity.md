# Activity performed as part of Light Room

- **Welcome** :
Scenario:
I am working on a database application called Light! Would you like to try it out?
If so, the application is running on port 1337. You can connect to it using nc <IP_Address> 1337
You can use the username smokey in order to get started.

Note: Please allow the service 2 - 3 minutes to fully start before connecting to it.

Questions:
1. What is the admin username?
2. What is the password to the username mentioned in question 1?
3. What is the flag?

- **Solution** :
1. Start the attack machine and the target machine.
2. Try pinging the target machine. command: "ping <IP_address>"
3. Start nmap scan to chekc the services running on the system. command: "nmap -p- -A -vv <IP_address>"
4. Although we see that the service run on the target are minimum and the details provided for the challenge is enough.
5. Connect to the target using the netcat command. command:"nc <IP_address> 1337"
6. As we are able to connect to target machine but it keeps asking for username.
7. As we got to know that the service running is database. Try to bypass and get the required result using many query string one among them is 'Union Select'.
8. Now to get the version running on the target, use the command 'Union Select version() '.
9. Now to get the tables present in the db, use the command 'Union Select group_conact(sql) FROM sqlite_master'
10. Now to get the table content in the db, use the command 'Union Select group_concat(col1 || ":" || col2) FROM table_name '
