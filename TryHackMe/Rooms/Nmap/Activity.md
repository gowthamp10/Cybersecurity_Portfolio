# Activity performed as part of Nmap Room

- **Practical module** :
1. Execute command "ping <IP>", to check if users are able to connect to the server/target.
2. Execute command "nmap -sX <IP>", to check the open|filtered ports from 1-999 Xmas Scan.
3. Execute command "nmap -sX -vv <IP>", to check the open|filtered ports from 1-999 Xmas Scan and high verbosity.
4. Execute command "nmap -sS -vv -p 1-5000 <IP>", to check the check for open ports using SYN SCAN and high verbosity.
5. Open wireshark on the attack machine and select the interface, Run the TCP Connect scan "nmap -sT -vv -p 80 <IP>", Observations were that the SYN->SYN/ACK->ACK handshake takes place as the port is open.
6. Execute command "nmap --script=ftp-anon -p 21 <IP>", provides result on service details on port 21 which uses FTP protocol and checks if anonymus login is possible.

