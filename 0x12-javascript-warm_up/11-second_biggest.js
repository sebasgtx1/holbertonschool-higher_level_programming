#!/usr/bin/node
let args = process.argv;
args = args.splice(2, args.length);
if (args.length < 2) {
  console.log(0);
} else {
  args = args.map(Number);
  args.sort(function(a, b){return b - a});
  console.log(args[1]);
}
