#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction.call(number + 1), this;
};
