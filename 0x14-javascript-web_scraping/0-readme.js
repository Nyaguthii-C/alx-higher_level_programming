#!/usr/bin/node
// reads and prints the content of a file
// where the content of the file must be read in utf-8

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, readData) {
  console.log(error || readData);
});
