#!/bin/bash
# send request to URL and display size of body of the response
curl -s "$1" | wc -c
