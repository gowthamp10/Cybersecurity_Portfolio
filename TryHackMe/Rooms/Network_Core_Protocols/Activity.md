# Activity performed as part of Network Core Protocols Room

- **Pre-requesite** :
1. Start the Attack Machine and the target machine provided for the room.

- **Task 1** :
1. Execute whois command on the attack machine for the domains x.com and twitter.com

- **Task 2** :
1. To connect to the telnet service offered by the target machine utilize the command telnet <IP_Address> 80.
2. Then utilize the GET method to get the flag.html file using the telnet service.
GET /Flag.html HTTP/1.1
Host: anything
Utilizing the above body mentioned. The required flag can be retrived. If Wrireshark is running parallely the captured data can be viewed.

- **Task 3** :
1. To connect to the FTP server running on the target machine utilize the command ftp <IP_Address>.
2. Provide username as anonymous and don't enter any password. User should be able to connect to ftp server as a anonymous user(usual misconfig on FTP servers).
3. Utilize the get command the retrive the file from the server to the local. Command: get <File_name>.

- **Task 4** :
1. Start the wireshark application to capture the conversation.
2. Connect to the SMTP service using the telnet command. Command: telnet <IP_Address> 25
3. Utilize the commands learnt and sample to send an email.
4. Analyze the traffic using wireshark.

- **Task 5** :
1. Start the wireshark application to capture the conversation.
2. Connect to the POP3 service using the telnet command. Command: telnet <IP_Address> 110
3. Utilize the credentials provided to login and sucessfully authenticate the user.
4. Utilize the commands learnt in POP3 section to get the flag.
5. Analyze the traffic using wireshark.
