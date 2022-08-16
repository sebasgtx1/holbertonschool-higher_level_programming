#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.filter((currentItem) => currentItem === searchElement).length;
};
