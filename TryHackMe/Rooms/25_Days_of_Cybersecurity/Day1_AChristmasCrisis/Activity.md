# Activity performed as part of Day 1 A Chirstmas Crisis Room

- **Phase Enumeration** :
1. Start the Attack Machine and Target Machine.
2. Open the Browser on the attack machine and provide the <IP_address> of the traget machine and land on the web-app.
3. Now, According to the story line all the services have been shutdown from the attacker. We should re-deploy all the services.
4. Create a user by providing username and password and click on Register.
5. Using previously provided username and password login.
6. Now, According to the read of Day 1 Theory. The session details are stored and maintained in cookies.
7. Navigate to Cookie and decode the value using the cyber-chef tool. As we see the encoding is of Hexadecimal upon using the From Hex option on the cyber-chef tool the value can be decoded.
8. Upon viewing the decoded information what is the key thing that gets highlighted? Ofcourse its the username that's part of the cookie value.

Further we use this details to exploit and gain access as Santa to bring the servers back-up.

- **Phase Exploitation** :
1. Now, modify the username to 'Santa' and convert the data into Hexadecimal using cyber-chef.
2. Now change the value of the cookie with the new value. Refresh the page to be recognized as Santa.
3. Now, Since you are Santa you should be able the bring up the services.
4. Upon bringing up all the service you will receive the flag.