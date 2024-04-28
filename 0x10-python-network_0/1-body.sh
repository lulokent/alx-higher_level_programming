#!/bin/bash
# A script that takes in a URL, send GET request to the URL, displays the body of the response
curl -sX GET "$1" -L 200
