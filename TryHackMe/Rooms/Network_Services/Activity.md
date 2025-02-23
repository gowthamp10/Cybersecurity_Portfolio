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
