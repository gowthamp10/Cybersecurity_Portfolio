# Activity performed as part of Network Secure Protocols Room

- **Task 1** :
1. Matching the protocols ports with secure-protocols ports.Below is the required knowledge as part of the activity.
List of unsecure portocols and there corresponding secure protocols.
Protocols           Unsecure_ports          Protocols           Secured_ports 
TELNET              23                      SSH                 22
HTTP                80                      HTTPS               443
SMTP                25                      SMTPS               465 and 587
POP3                110                     POP3S               995
IMAP                143                     IMAPS               993
FTP                 21                      FTPS                990

- **Task 2** :
1. Start the Machine provided as part of the activity.
2. Although the command is executed and keys are extracted. Command which was utilized is command: "chromium --ssl-key-log-file=~/ssl-key.log".
3. Open the pcapng file in wireshark and provide the key to decrypt the log. Steps used to provide the key to decrypt are as follows:
3.1 Right-clicking anywhere, choose “Protocol Preferences.” From the submenu, select “Transport Layer Security.” Thirdly, click on “Open Transport Layer Security preferences.”
3.2 Clicking “Open Transport Layer Security preferences” will show a dialog box. You must click the “Browse” button marked with four to locate the ssl-key.log. Click on OK.
4. Go through the network log to find the login credentials.

