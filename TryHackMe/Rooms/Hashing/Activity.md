# Activity performed as part of Hashing Room 

- **Task 2** :
1. Run the command:"sha256sum <file_name>". To get the hash of the desired file.

- **Task 3** :
1. Run the command: "head <file_name> -n 20", To get the 20 line output the filename provided.

- **Task 6** :
1. Idetity the type of hash algorithm used as part creating the hash value from the hash using the previous task contents. Run the command: "hashcat -m 3200 -a 0 <file_location> usr/share/wordlists/rockyou.txt". The craked hash value provide some thing like this <Hash>:<Original_string>.
2. As the algorithm used was already meantion and the hash mentioned was not of structure $<v1>$<v2>$<v3>. Run the command: "hashcat -m 1400 -a 0 <file_location> usr/share/wordlists/rockyou.txt". The craked hash value provide some thing like this <Hash>:<Original_string>.
3. Idetity the type of hash algorithm used as part creating the hash value from the hash using the previous task contents. Run the command: "hashcat -m 1800 -a 0 <file_location> usr/share/wordlists/rockyou.txt". The craked hash value provide some thing like this <Hash>:<Original_string>.
4. Used online tool: hashes.com to crack the final hash mentioned as the hint suggested the use of online tool.

- **Task 7** :
1. Run the command: "sha256sum <file_name>", Provides the hash of the file.
2. Run the command: "man hashcat | grep HMAC", Provides outpout having string match of HMAC and HMAC SHA512 (key = $pass) can be found.

- **Task 8** :
1. Run the command: "base64 -d <file_name>", to decode the base64 encoded string back to plain text.

