#!/bin/bash
# A script that takes in a URL as an argument, send a GET requesr to the URL
# and display the body of the response
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
