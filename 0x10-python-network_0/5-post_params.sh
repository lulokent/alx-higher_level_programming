#!/bin/bash
# A script that takes in a URL,sends a POST request to the passed URL
# displays the body of response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
