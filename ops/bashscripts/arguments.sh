#!/bin/bash

echo "Default Command Line Arguments can be accessed by \$0 to \$9"

echo "Argument 0 is \$0, Argument 1 is \$1."

echo "Argument 0 will always have the script name"

echo "Argumnents are provided in the order they are given e.g. ./arguments.sh 1 2 3"

echo -e "\n\nArgument 0 is:\n"
echo $0

echo -e "Argument 1 is:\n"
echo $1

echo -e "Argument 2 is:\n"
echo $2