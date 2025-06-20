# Activity performed as part of John the Ripper: The Basics 

- **Pre-requisite** :
Use the VM provided for the room.

- **Task 4** :
1. Check out few things before cracking the hashes. check out the hash-id.py file, help page of john.
2. To find the hash type of run the python file and provide all the four hash values as input to the script one after another.
3. To crack the hash use the following command: "john --format=<hash_type> --wordlist=/usr/share/wordlists/rockyou.txt <hash_file>".
4. For few of the <hash_type>, the need of raw- prefix can be checked using command:"john --list=formats | grep -iF "<hash_type>".

- **Task 5** :
1. Start deducing the hash type of the hash value provided. According to the information provided I deduced it as NT.
2. Run the command: "john --format=<Hash_Type> --wordlist=/usr/share/wordlists/rockyou.txt <File>". To get the cracked hash value.

- **Task 6** :
1. In order to perform the unshadowing process use the command: "unshadow <local_passwd> <local_shadow> > <unshadow_file>".
2. In order to crack the hash use the command: "john --format=<Hash_type> --wordlist=<wordlist_location> <unshadow_file>"

- **Task 7** :
1. Identify the hash type using the hash-id.py provided in VM.
2. Using the single crack mode crack the password on the hash whose user is Joker. Use the command: "john --single --format=<hash_type> <hash_file>". Remember to modify the hash file prefixing username:<hash>.

- **Task 9** :
1. Check all available option of the zip2john tool. Using the command: "zip2john -h".
2. Now utilizing the command: "zip2john -s <zipfile> > <outputfile>". The command provides hash format that can be understood by john.
3. Run command: "john --wordlist=/usr/share/wordlists/rockyou.txt <outputfile>". Cracks the has based on the provided hash file.
4. Utilize the password to unzip the zip file and get the flag.

- **Task 10** :
1. Now utilizing the command: "/opt/jhon/rar2john <rarfile> > <outputfile>". The command provides hash format that can be understood by john.
2. Run command: "john --wordlist=/usr/share/wordlists/rockyou.txt <outputfile>". Cracks the has based on the provided hash file.
3. Utilize the password to unrar the rar file and get the flag.

- **Task 11** :
1. Now utilizing the command: "python3 /opt/jhon/ssh2john <privatekey> > <outputfile>". The command provides hash format that can be understood by john.
2. Run command: "john --wordlist=/usr/share/wordlists/rockyou.txt <outputfile>". Cracks the has based on the provided hash file and and gives the plaintext value of the privatekey.
