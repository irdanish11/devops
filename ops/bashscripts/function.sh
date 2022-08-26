#!/bin/bash

age_name() {
    age=$1
    name=$2
    if [[ $age -le 18 ]]
    then
        echo "$name you are under 18"
    elif [[ $age -gt 18 ]] && [[ $age -lt 40 ]]
    then
        echo "$name you are between 18 and 39"
    elif [[ $age -ge 40 ]] && [[ $age -lt 60 ]]
        echo "$name you are between 40 and 59"
    then
        echo "$name you are over 60"
    fi
}

age_name 26 "Irfan"