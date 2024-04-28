#!/bin/bash
# A script that takes in a URL as an argument, send a GET requesr to the URL
# and display the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98"
