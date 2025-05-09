# Activity performed as part of NetSec Challenge Room

- **Pre-requesite** :
1. Start the attck machine and target machine provided for the room.

- **Nmap Task** :
1. Execute an nmap scan using -p-, -A, -vv option on the target and store it in a file.
Command: "nmap -p- -vv -A <IP_Address> > <File_name>"
2. Utilize the scan data to answer the questions.

- **Hydra Task** :
1. As there 2 users provided in question utilize hydra to brute-force password guessing. Utilize the below command.
Command: "hydra -l <username> -P <Password_possible_list_available> -s <PORT> <IP_address> ftp"
2. Utilize the passwords found from the command to get the flag from the ftp server.

- **Firwall/IDS evasion using Nmap** :
1. Try-out possible nmap options availabe utilize the command:"man nmap" to get the manual page of the nmap tool.
2. The command that worked out was null scan -sN.
Command: "nmap -sN <IP_Address>"

Note: If you are wondering why telnet was not ustilized to get the HTTP header flag. It's just that the nmap scan provided the flag and performing same task to get the flag would not be efficient.

