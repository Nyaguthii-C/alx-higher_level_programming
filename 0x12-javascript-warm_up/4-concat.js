#!/usr/bin/node

/* prints two arguments passed to it, in the following format: “ is ” */
const args = process.argv;
const firstArg = args[2];
const secondArg = args[3];
console.log(firstArg + ' is ' + secondArg);
