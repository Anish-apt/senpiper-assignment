#!/bin/bash

response=$(grep -e 'HTTP/1.1" 200' -e 'HTTP/1.0" 200' access.log | wc -l)

echo "Total logs count with successful response (status code: 200) : ${response}"
