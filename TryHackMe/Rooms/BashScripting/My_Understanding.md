Contents of the room
1. Introduction to Bash scripting
2. Our first sample bash script
3. Variables
4. Parameters
5. Arrays
6. Conditional Statements

Introduction to Bash scripting

What is bash?
Bash is a scripting language that runs within the terminal on most Linux distros and MacOS. Shell scripts are a sequence of bash commands within a file, combined to achieve more complex tasks than simple one-liners, and are especially useful when automating sysadmin tasks such as backups.

The basic structure of a bash script 
The script always starts with #!/bin/bash as its first line and the rest of the task/script comes next.

Variables
using variables all sorts of values can be stored. Saving the value there should be no space between the assignment operator and value and variable name, for using the variable ($)var_name '$' is a must.
The primary thing used to debug a script is set - x and set +x
Running a bash script command: bash -x ./<file_name>.sh



