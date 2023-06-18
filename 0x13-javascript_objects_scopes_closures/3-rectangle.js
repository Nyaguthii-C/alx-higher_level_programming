#!/usr/bin/node
/* Create an instance method called print()
* that prints the rectangle using the character X
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let Xter = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        Xter += 'X';
      }
      console.log(Xter);
      Xter = '';
    }
  }
};
