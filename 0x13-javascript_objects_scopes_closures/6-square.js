#!/usr/bin/node
/**
* Create an instance method called charPrint(c)
* that prints the rectangle using the character c
* If c is undefined, use the character X
*/
module.exports = class Square extends require('./4-rectangle.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let XterC = '';
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          XterC += 'C';
        }
        console.log(XterC);
        XterC = '';
      }
    }
  }
};
