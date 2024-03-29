#!/usr/bin/node
/* Create an instance method called rotate()
* that exchanges the width and the height of the rectangle
* Create an instance method called double()
* that multiples the width and the height of the rectangle by 2
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

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }
};
