#!/usr/bin/node

/* a script that prints a message depending of the number of arguments passed */
const args = process.argv;
if (args.length <= 2) {
  const noArgs = 'No argument';
  console.log(noArgs);
} else if (args.length === 3) {
  const oneArg = 'Argument found';
  console.log(oneArg);
} else if (args.length >= 4) {
  const multiArgs = 'Arguments found';
  console.log(multiArgs);
}
