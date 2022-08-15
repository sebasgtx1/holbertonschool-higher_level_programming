#!/usr/bin/node
const args = process.argv;
const myNumber = Math.floor(Number(args[2]));
if (args[2] && !Number.isNaN(myNumber)) {
  console.log('My number: ' + myNumber);
} else {
  console.log('Not a number');
}
