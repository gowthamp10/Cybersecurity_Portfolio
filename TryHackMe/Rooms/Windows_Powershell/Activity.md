# Activity performed as part of Window Powershell Room

- **Phase 1** : 
1. Connecting to the lab machine provided using the attack-box.
2. Start both lab machine and the attack-box machine.
3. Click on Applications menu -> Internet -> Remmina.
4. Click on cancel for the pop-up window prompt(Login Keyring).
5. Slelct the ssh option, provide the IP address of the lab machine.
6. Enter the user name and password for window-pop and click on OK button.
7. Run powershell command to navigate to the (PS) prompt.
8. Run Get-Command cmdlet, to check which are all the possible cmdlets that can be used by the user. Command Info object is retrived to get the essential properties of the cmdlets.
9. Run Get-Command -CommandType "Function", lists all the command-lets having the command type of function.
10. Run Get-Help cmdlet,to provides detailed information about cmdlets, including usage, parameters, and examples.
11. Run Get-Help Get-Command cmdlet, to provides detailed information about Get-Command cmdlet(Name, Synopsis, Description, Related links, Remarks).
12. Run Get-Help Get-Command -Examples cmdlet, to provides detailed information about Get-Command cmdlet(Name, Synopsis with examples).
13. Run Get-Alias cmdlet, to get list of all available alias.

-- Can't be performed on the lab machine:
1. Run Find-Module -Name Power*, to find remote repositories of Command let starting with Power.
2. Run Install-Module -Name PowerShellGet, to download the cmdlet to the local machine.

- **Phase 2** : 
1. Execute the command "Get-ChildItem", to get the directories  and files in the current working directory.
2. Execute the command "Get-ChildItem -Path "C:\Users"", to get the directories  and files in the path: C:\Users.
3. Execute the command "Set-Location -Path "\Document"", to naviagte to the Document directory.
4. Execute the command "New-Item -Path "Test.txt"", creates a new file in the currently working directory having the name Test.txt.
5. Execute the command "Remove-Item -Path "Test.txt"", deletes the file in the currently working directory having the name Test.txt.
6. Execute the command "Copy-Item -Path <File_Location> -Destination <Destination_Location>", copies the file mentioned in <File_Location> to <Destination_Location>.
7. Execute the command "Move-Item -Path <File_Location> -Destination <Destination_Location>", copies the file mentioned in <File_Location> to <Destination_Location>.

- **Phase 3** : 
1. Execute the command "Get-ChildItem | Sort-Object Length", to get files and directories sorted with length in asc order. 
2. Execute the command "Get-ChildItem | Where-Object -Property "Length" -gt 100", to get the files and directories having size/length greater than 100.
3. Execute the command "Get-ChildItem | Select-Object Name,Length", to get the files and directories but only there Name and Length with no other properties.
4. Execute the command "Get-ChildItem | Sort-Object Length -Descending | Select-Object -First 1", to get the largest file in the currently working directory.
5. Execute the command "Select-String -Path <File_name> -Pattern <string_pattern>", to get the lines in the file with the occurance of <string_pattern>.

- **Phase 4** : 
1. Execute the command "Get-ComputerInfo", to get the basic information about the machine.
2. Execute the command "Get-localUser", providers list of users present on the machine and there properties.
3. Execute the command "Get-NetIPConfiguration", provides details on network interfaces on the system, IP addess etc.
4. Execute the command "Get-NetIPAddress", provides all the details on IP addresses configured on the system and irrespective of the current status.
5. Execute the following commands to get the flag for the question meentioned.
    5.1 "Set-Location "C:\Users\<user>"", to navigate to the <user> users location on the users directory.
    5.2 "Get-ChildItem", to view all the files and directories present in the current working directory.
    5.3 "Get-Content <file_name>", to get the flag present in the file.

- **Phase 5** :
1. Execute the command "Get-Process", to get all the currently running processes on the sytem.
2. Execute the command "Get-Service", to get all the services that are running, stopped and paused.
3. Execute the command "Get-NetTCPConnection", to get all the TCP connections with both local and remote endpoints.
4. Execute the command "Get-FileHash -Path <File_path>\<File_name>", to get the hash on the <File_name> mentioned.

- **Phase 6** :
1. Execute the command "Get-Help Invoke-Command -examples", to get the examples usage of the command to understand better.

