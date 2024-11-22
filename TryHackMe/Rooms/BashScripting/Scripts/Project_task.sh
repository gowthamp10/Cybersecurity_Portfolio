#!/bin/bash
filename=$1
if [ -f $filename ] && [ -w $filename ]
then
  echo "Hello" > $filename
else
  touch "$filename"
  echo "Hello" > $filename
fi
echo "Enter your Name:"
read name
echo "Enter your Age:"
read age
if [ $age -ge 18 ]
then
  echo "Name:" $name "Age:" $age" Yay eligile for working "
else
  echo "Name:" $name "Age:" $age" Sorry not eligile for working "
fi

  
