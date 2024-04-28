#!/bin/bash
# A script that takes in URL,sends a request to that URL,and displays the size of the body
curl -sI GET "$1" | grep -i "Content-length" | cut -d " " -f 2
