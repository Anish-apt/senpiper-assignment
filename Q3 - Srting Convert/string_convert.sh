#!/bin/bash

response=$(echo "Ab1Cd2Ef3Gh4Ij5" | sed 's/[A-Z]/\L&/g' | sed 's/[0-9]*//g')

echo "The converted string of Ab1Cd2Ef3Gh4Ij5 is: ${response}"
