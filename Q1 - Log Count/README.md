# Usage

The command to count the log statements in the `access.log` file is:

```
grep -e 'HTTP/1.1" 200' -e 'HTTP/1.0" 200' access.log | wc -l
```

We grep the status code 200 strings and then pipe it to word count command with `-l` argument to count the number of log statements.