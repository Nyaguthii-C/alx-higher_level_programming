#!/usr/bin/node
//reads and prints the content of a file
//where the content of the file must be read in utf-8


var fs = require("fs");
var data = process.argv[3]

fs.writeFile(process.argv[2], data , error => {
  if (error)console.log(error);
});

