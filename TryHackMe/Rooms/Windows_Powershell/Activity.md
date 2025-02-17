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
6. 
