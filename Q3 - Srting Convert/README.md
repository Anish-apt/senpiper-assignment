# Usage

The sed command to to convert the string input "Ab1Cd2Ef3Gh4Ij5..." to "abcdefghij..." is: 

```
echo "Ab1Cd2Ef3Gh4Ij5" | sed 's/[A-Z]/\L&/g' | sed 's/[0-9]*//g'
```

We are passing the input string to first sed command which will convert the upper case alphabets to lower case alphabets then we are passsing that output to another sed command which will remove the numerical digits in the string.