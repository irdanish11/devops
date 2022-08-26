#!/bin/bash

i=0

while [[ $i -lt 10 ]]
do
    echo $i
    i=`expr $i + 2`
    #i=$(($i+2))
done