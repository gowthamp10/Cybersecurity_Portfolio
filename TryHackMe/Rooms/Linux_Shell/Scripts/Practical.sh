#!/bin/bash

#Defining the directories to search
directory = 

#Defining flag to search
flag = 

echo "Flag searching in $directory in progress"

#Defining loop to iterate through out all the log files
for file in "$directory"/*.log;
do 
    #Check if file contains flag
    if grep -q "$flag" "$file"; then
        #Print the filename
        echo "Flag found in: $(basename "$file")"
    fi  
done

