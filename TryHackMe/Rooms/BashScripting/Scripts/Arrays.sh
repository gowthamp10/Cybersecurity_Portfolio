#!/bin/bash
transport=('car' 'bus' 'train' 'metro' 'auto')
echo "Array Tansport: "${transport[@]} #prints all the content of the array. Here, @ means all and enclosed with [] specifies indexes
#Output Car
echo "Array at 0:" ${transport[0]}
#Unset value for auto and then replace it with glider
unset transport[4]
transport[4]='glider'
echo "Array Tansport: "${transport[@]}
