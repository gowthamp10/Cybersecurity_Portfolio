# Activity performed as part of Window Command Line Room

- **Phase 1** : 

1. Connect to the VM provided for the Room using the command: ssh user@<ip>
2. Execute set command on the windows cli, and check out the path variable.
3. Execute ver command on the windows cli, and check out the OS version.
4. Execute systeminfo command on the windows cli, and check out the system information like hostname, version, etc.
5. Execute driverquery command on the windows cli, and check out the details the installed device drivers.

- **Phase 2** : 

Network configuration
1. Execute ipconfig command on the windows cli, and check out the network configuration on the system.
2. Execute ipconfig /all command on the windows cli, and check out the all network configuration on the system.

Network Troubleshoot
1. Execute ping <traget_name> command on the windows cli, and check out if the server is responding to ICMP request which is also called a ping.
2. Execute tracert <traget_name> command on the windows cli, and check out the trace route of a domain.

More Networking Commands
1. Execute nslookup <traget_name> command on the windows cli, and check out IP address of the domain. 
2. Execute nslookup <traget_name> <IP_address> command on the windows cli, and check out IP address of the domain. The IP_address is nothing but the name server.
3. Execute netstat command on the windows cli, and check out the current network connections and listening ports.
4. Execute netstat -h command on the windows cli, and check out the help page of the netstat command.
5. Execute netstat -abon command on the windows cli, and check out -a displays all established connections and listening ports, -b shows the program associated with each listening port and established connection, -o reveals the process ID (PID) associated with the connection, -n uses a numerical form for addresses and port numbers.

- **Phase 3** : 

Working With Directories
1. Execute cd command on the windows cli, and check out current location. 
2. Execute dir command on the windows cli, and check out the child directories of the current location.
3. Execute dir /a command on the windows cli, and check out the all the files including hidden and system files of the current location.
4. Execute dir /s command on the windows cli, and check out the all the files of the current location and the sub-directories.
5. Execute tree command on the windows cli, and check out file structure.
6. Execute cd <Traget_directory> command on the windows cli, and check out navigate to the <Target_directory>.
7. Execute mkdir <directory_name> command on the windows cli, and create a new directory named <directory_name>.
8. Execute rmdir <directory_name> command on the windows cli, and delete the directory named <directory_name>.

Working With Files
1. Execute type <file_name> command on the windows cli, and all the content of the file is to displayed on the terminal. Suggested to be used for small files.
2. Execute more <file_name> command on the windows cli, and page specific content of the file is dispalyed starting from page 1. Suggested to be used for large files.
3. Execute copy <file_name> <location> command on the windows cli, and specific file named <file_name> is copied to specific location named <location>.
4. Execute move <file_name> <location> command on the windows cli, and specific file named <file_name> is moved to specific location named <location>.
5. Execute del/erase <file_name> command on the windows cli, to delete the specific file named <file_name>.
6. Execute copy <Wild_card><partial_file_name> <location> command on the windows cli, and specific files that match the wildcard and partial filename <Wild_card><partial_file_name> is copied to specific location named <location>.

To get the flag required for the question the following commands needs to be executed:
1. Use cd C:\Treasure\Hunt command to navigate to the target location.
2. use dir command to check the files and sub-directories present in the location. Check the flag.txt file content using the type command.
3. use type flag.txt to get the flag displayed on the terminal.

- **Phase 4** :

Task and Process Management
1. Execute tasklist command on the windows cli, and check out running processes on the system. 
2. Execute tasklist /? command on the windows cli, and check out all the available filtering options.
3. Execute tasklist /FI "imagename eq sshd.exe" command on the windows cli, and check out the process running ssh.
4. Execute taskkill /PID 1516 command on the windows cli, and kill the process associated with PID = 1516.
5. Execute tasklist /FI "imagename eq notepad.exe" command on the windows cli, and check out if any process is running related to notepad.

- **Phase 5** :

Conclusion
1. Execute shutdown /? | more command on the windows cli, and check out the help page of the shutdown command. 
