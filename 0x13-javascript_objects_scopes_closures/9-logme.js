#!/usr/bin/node
let argp = 0;

exports.logMe = function (item) {
  console.log(argp + ': ' + item);
  argp++;
};
