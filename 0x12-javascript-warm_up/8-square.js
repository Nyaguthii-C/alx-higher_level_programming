#!/usr/bin/node

/* prints a square */
const args = process.argv;
const size = args[2];
let Xter = '';
/* define limits for length and width */
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    Xter += 'X';
  }
  /* print the square after iterating */
  console.log(Xter);
  /* reset character to empty after printing */
  Xter = '';
}
if (isNaN(size)) {
  console.log('Missing size');
}
