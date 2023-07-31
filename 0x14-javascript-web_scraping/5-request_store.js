#!/usr/bin/node
// a script that gets the contents of a webpage and stores it in a file
// Use streaming to stream response to a file stream
const request = require('request');
const url = process.argv[2];
const fs = require('fs');

request(url).pipe(fs.createWriteStream(process.argv[3]));
