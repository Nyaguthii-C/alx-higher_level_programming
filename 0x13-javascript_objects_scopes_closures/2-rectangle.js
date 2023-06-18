#!/usr/bin/node
/* set the function to  create an empty object
* if w or h is equal to 0 or not a positive integer
*/
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
};
