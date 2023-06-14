#!/usr/bin/node

/* prints the first argument passed to it */
const args = process.argv;
const firstArg = args[2];
if (firstArg) {
  console.log(firstArg);
} else {
  console.log('No argument');
}
