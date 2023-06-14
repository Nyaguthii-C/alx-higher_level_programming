#!/usr/bin/node

/* prints x times “C is fun” */
const args = process.argv;
const myStr = 'C is fun';
const counts = args[2];
if (isNaN(counts)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= counts; i++) {
    console.log(myStr);
  }
}
