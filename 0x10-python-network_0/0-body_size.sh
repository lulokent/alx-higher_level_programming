#!/usr/bin/bash
# A scriot that takes in URL,sends a request to that URL,and displays the size of the body
curl -sI "$1" | grep "Content-length:" | cut -d " " -f 2
