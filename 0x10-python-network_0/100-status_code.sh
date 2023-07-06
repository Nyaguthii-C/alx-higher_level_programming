#!/bin/bash
# send request to URL and display only status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
