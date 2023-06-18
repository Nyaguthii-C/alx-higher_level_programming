#!/usr/bin/node
/* add a constructor and initialize width and height instance attributes */
module.exports = class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
};
