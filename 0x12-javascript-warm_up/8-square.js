#!/usr/bin/node

/* prints a square */
const args = process.argv;
const size = args[2];
let Xter = '';
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    Xter += '#';
  }
  Xter += '\n';
}
console.log(Xter);
