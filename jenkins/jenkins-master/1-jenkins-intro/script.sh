#!/bin/bash

NAME=$1
LAST_NAME=$2
SHOW=$3

if [ "$SHOW" = "true" ]; then
    echo "Hello, my name is $NAME $LAST_NAME"
else
    echo "To print the name set show option to true."
fi
