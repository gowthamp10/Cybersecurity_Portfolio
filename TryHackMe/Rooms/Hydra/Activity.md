# Activity performed as part of Hydra Room 

- **Pre-requisite** :
1. Start both the target and the Attack box.

- **Using Hydra** :
1. Starting with web-request brute force password cracking tool.
2. Use command:"hydra -l <username> -P <passwordlist> <Targetdomain/IP> http-post-form "/<targetpath>:username=^USER^&password=^PASS^:F=<Error_message>" -V". Upon using the command hydra tries to login using the list of passwords provided to get the valid password.
3. Login to the application using the cracked password to get the flag.
4. Use command:"hydra -l <usernname> -P <Passwordlist> -t 4 ssh://<IP>". To brute force crack the password of the target which is used for SSH protocol.
5. Login using SSH to get the flag.
