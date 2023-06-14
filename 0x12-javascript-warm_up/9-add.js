#!/usr/bin/node

/* a script that prints the addition of 2 integers */
const args = process.argv;
function add (a, b) {
  return (a + b);
}
const a = parseInt(args[2]);
const b = parseInt(args[3]);
console.log(add(a, b));
