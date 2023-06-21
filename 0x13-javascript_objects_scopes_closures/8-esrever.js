#!/usr/bin/node
/* a function that returns the reversed version of a list */
exports.esrever = function (list) {
  const revdlist = [];
  let i;

  for (i = list.length - 1; i >= 0; i--) {
    const j = list[i];

    revdlist.push(j);
  }

  return (revdlist);
};
