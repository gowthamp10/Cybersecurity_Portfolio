# Activity performed as part of Active Directory Basics Room

- **Phase 1** :

Create an OU in the Machine provided as part of the excercise. The OU named 'Students' was created.

- **Phase 2** :

Change in Organizational stucture are as follows
1. Management Daniel(General Manager)
2. Marketing Mark(Marketing Specialist)
3. Sales Sophie(Sales Director)
4. Sales Thomas(Sales Rep.)
5. IT Phillip(IT Support)
6. IT Mary(Server Admin)
7. IT Clarie(Domain Admin)

Ckeck the OU's present on the machine associated with room and make the necessary Change by deleting the extra OU found on the machine.
OU's are protected against accidental deletion. For a user to delete the OU following steps must be completed before attempting deletion.
1. Click on View on the Top menu bar available in the Application.
2. Click on Advanced features.
3. Right click on the OU and navigate to properties.
4. Navigate to the Object tab of the Properties window.
5. Uncheck the 'Protect object from accidental deletion'
6. Apply and save the changes.

- **Phase 3** :

Providing Delegation to Phillip(IT Support), The following are steps to delegate control.

1. Select the OU which needs to have the Delegation of Control.
2. Right Click, Select Delegate control.
3. Window pop-up of Delegation of Control Wizard opens up.
4. Click the next button.
5. Click on Add, present on the Users and Groups Page of the Wizard.
6. To avoid miss-typing after specifying the name, Click on the Check Names button.
7. Click on Ok button, then Click on Next button.
8. Since, the task is about reset of passwords. Select the checkbox and click on Next and complete the process.

**Challenge**

I was stuck at the login to philip's Account which is remote desktop. So went through the walkthrough over youtube to better understand on how to login as Phillip.

**Solution**

I was supposed to login top phillip's account through the attack box and not the machine provided for the acitivity.
Steps to login:
1. Install xfreerdp on attack machine one time step.
2. use the command xfreerdp <IP>.
3. Now, windows pop-up of RDP opens, use username:THM\phillip and password:Clarie2008 to login.

 **Continuing phase 3**
According to the activity open the powershell andf enter the command provided in the activity.
command: Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose

After running the command enter the password.Run an additional command such that the user should reset the password upon login.
command: Set-ADUser -ChangePasswordAtLogon $true -Identity sophie -Verbose

After that user should login to sophie's account using the default credentials set by phillip. Once, trying to login user would be asked to reset the password because of the configuration done by phillip.

Upon opening sophie's system, submit the flag which is present on the desktop in the file named flag.

- **Phase 4** :
All the machine associated to the domain or not segregated to have unique groups and policies. Lets segregate to have a better handle of the security posture.

This is done by creating new OU's under the domain and moving the Machines available in the Computers container.

- **Phase 5** :
Edit a GPO, according to the activity the Default domain policy GPO is what needs to be edited.

The following is the changes that needs to be made.
1. change the minimum password length policy to require users to have at least 10 characters in their passwords.

Steps to make the changes.
1. Open the Group Policy Management tool.
2. Click on Group Policy Objects.
3. Click on the Default Domain Policy.
4. Right-click on the Default Domain Policy and select Edit.
5. Now, navigate to the following path on the new window pop-up(Group Policy Management Editor) Path: Computer Configurations -> Policies -> Windows Setting -> Security Settings -> Account Policies -> Password Policy.
6. Double click on policy Minimum Password Lenght.
7. In the new pop-up window(Minimum Password Lenght Properties) increase the lenght to 10. Then click on OK.

- **Phase 6** :
Adding new GPO, to the existing list.

Task:
1. Block non-IT users from accessing the Control Panel.
2. Make workstations and servers lock their screen automatically after 5 minutes of user inactivity to avoid people leaving their sessions exposed.

Restrict Access to Control Panel
Steps to restrict access to control panel:
Pre-requsite: Open Group Policy Management.
1. Right-click on the Group Plolicy Objects, Select create new GPO and name it Restrict Control Panel Acess.
2. Navigate to the new GPO created and click on Edit. Group Policy Management Editor window pop-up will open. 
3. Navigate to the User Configuration since the configuration change is for users.
4. Navigate to the following path: User Configurations -> Policies -> Administrtive Templates -> Control Panel to locate 'Prohibit access to Control Panel and PC settings'.
5. Make the changes to 'Prohibit access to Control Panel and PC settings' by enabling it and click on apply and ok.
6. Close the Group Policy Management Editor window. Navigate to Group Policy Management. Drag and drop the policies to all the No/IT users group.

Auto Lock Screen GPO
Steps to Auto Lock Screen GPO:
Pre-requsite: Open Group Policy Management.
1. Right-click on the Group Plolicy Objects, Select create new GPO and name it Auto Lock Screen.
2. Navigate to the new GPO created and click on Edit. Group Policy Management Editor window pop-up will open. 
3. Since this is part of computer configuration Navigate to the following location: Computer Configurations -> Policies -> Windows Settings -> Security Settings -> local policies -> Security Options and find 'Interactive logon: Machine inactivity limit'.
5. Make the changes to 'Prohibit access to Control Panel and PC settings' by enabling it and click on apply and ok.
6. Close the Group Policy Management Editor window. Now drag and drop the policy over the domain as its computer configuration changes the policies would be ignored by users.

Verfying the changes made to the GPO by logging in to MARK's account.
Steps:
1. Login to the RDP.
2. Try launching Control Panel. The Control Panel should not launch and additional a dialog box should pop-up.
3. Leave it inactive for 5 mins it should ask for login.








