# Activity performed as part of "Protocols and Servers" Room

- **Pre-requsite** :
Start the Attack Machine and Target Machine provided.

- **Hypertext Transfer Protocol (HTTP)** :
1. First, we connect to port 80 using telnet <Target_IP_Address> 80.
2. Next, we need to type GET /flag.thm HTTP/1.1 to retrieve the page flag.thm 
3. Finally, you need to provide some value for the host like host: telnet and press the Enter/Return key twice.

- **File Transfer Protocol (FTP)** :
1. Connect to the provided traget machine using the command: ftp <IP_Address>.
2. Provide username and password to login.
3. use "ls" command to list all the files on the ftp server.
4. use "get <file_name>" command to get the required file on to local machine.

- **Simple Mail Transfer Protocol (SMTP)** :
1. Connect to the provided target using "telnet <IP_Address> 25" command.
2. Check out the mail server using few commands like "helo hostname", "mail from:<mail_id>" etc.

- **Post Office Protocol 3 (POP3)** :
1. Connect to the provided target using "telnet <IP_Address> 110" command.
2. Utilize the credentials provided to authenticate.
3. Use STAT command to check the number of mails present and size of the inbox in octet.

- **Internet Message Access Protocol (IMAP)** :
1. Connect to the provided target using "telnet <IP_Address> 143" command.
2. Utilize the credentials provided to authenticate.
3. Check the sync across multiple devices.
4. Check Inbox for any new mails.

