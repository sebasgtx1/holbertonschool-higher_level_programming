#!/usr/bin/node
let args = process.argv;
if (args.length <= 3) {
  console.log(0);
} else {
  args = args.splice(2, args.length);
  args = args.map(Number);
  const max = Math.max(...args);
  args.splice(args.indexOf(max), args.indexOf(max) - 1);
  console.log(Math.max(...args));
}
