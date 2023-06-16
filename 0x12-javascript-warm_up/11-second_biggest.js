#!/usr/bin/node

/* searches the second biggest integer in the list of arguments */
const args = process.argv;
if (args.length <= 3) {
  console.log(0);
}
const myArgs = [];
if (args.length > 3) {
  for (let i = 0; args[i]; i++) {
    if (!(isNaN(args[i]))) {
      myArgs.push(args[i]);
    }
  }
  myArgs.sort();
  const secLast = myArgs.slice(-2, -1);
  console.log(secLast[0]);
}
