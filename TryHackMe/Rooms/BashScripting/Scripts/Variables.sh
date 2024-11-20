#!/bin/bash
name="Jackie"
echo $name

# To debug use set -x and set +x
set -x
num1=3
num2=5
echo "number 1:" $num1
echo "number 2:" $num2
echo "Product:" $(expr $num1*$num2)
set +x

