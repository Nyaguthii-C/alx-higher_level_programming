#!/usr/bin/node

/**
* prints My number: <first argument converted in integer>
* if the first argument can be converted to an integer
*/
const args = process.argv;
const myString = 'My number: ';
const firstArg = parseInt(args[2]);
if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log(myString + firstArg);
}
