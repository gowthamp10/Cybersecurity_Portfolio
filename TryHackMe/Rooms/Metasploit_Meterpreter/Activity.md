# Activity performed as part of Metasploit: Meterpreter

- **Pre-requisite** :
1. Start both the target VM and Attack Machine.

- **Post-Exploitation Challenge** :
1. Use the module: exploit/windows/smb/psexec to gain meterpreter shell with initail exploitation with provided credentials. Make sure all necessary parameters are provide for the exploitation process using the show options command and run the module using run/exploit command.
2. Use the meterpreter shell to get further details now.
3. Run the sysinfo command to get more information on the traget system.
4. Make the meterpreter session as a background process using Ctrl+Z. Then use the module: post/windows/gather/enum_shares to get the share folders avaiable on the target.
5. Now inorder to get the NTLM has of specific user we need to migrate to a different process. Get back into the session using the command: session -i <num>. Then run the ps command to get the list of all process migrate to lsass.exe process id using command: migrate <pid>.
6. run hashdump command. To get the hashdump of all the users on the target.
7. Use the crackstation tool to crack the hash.
8. To find the <file>. Use the command: search -f <file>.
9. To read the contents of the file use the command: cat '<Path>'
