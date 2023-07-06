#!/bin/bash
#sends a request to a URL passed as an argument, and displays only the status code of the response

response=$(curl -s -X POST 0.0.0.0:5000/catch_me)

if [[ $response == *"You got me!"* ]]; then
  printf "%s\n" "Server response: $response"
else
  printf "%s\n" "Failed to capture server response."
fi
