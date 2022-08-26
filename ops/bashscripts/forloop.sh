#!/bin/bash
echo "Bash version ${BASH_VERSION}"
for i in {0..10..2}
do
    echo "Welcome $i times"
done

for (( c=1; c<=5; c++ ))
do  
   echo "Welcome $c times"
done