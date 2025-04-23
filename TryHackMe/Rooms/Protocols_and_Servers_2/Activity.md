# Activity performed as part of "Protocols and Servers 2" Room

- **Pre-requsite** :
Start the Attack Machine and Target Machine provided.

- **Password Attack** :
1. Start wireshark application to capture network traffic.
2. Utilize Hydra for brute force attack on the target system with IMAP service command:"hydra -l lazie -P /usr/share/wordlists/rockyou.txt <IP_Address> imap".
3. Once password is found, Enter Ctrl+C to stop the brute-force attack.
4. Stop the wireshark capture, filter based on imap protocol and find the successful login stream.

