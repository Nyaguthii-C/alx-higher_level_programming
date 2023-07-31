#!/usr/bin/node
//writes a string to a file

var fs = require("fs");
var data = process.argv[3]

fs.writeFile(process.argv[2], data , error => {
  if (error)console.log(error);
});

