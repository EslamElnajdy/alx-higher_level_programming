#!/usr/bin/node
const arg = process.argv[2];
let num = parseInt(arg, 10);
let out = 'C is fun';
console.log(num);
if (isNaN(num)) {
  out = 'Missing number of occurrences';
  num = 1;
}
for (let i = 0; i < num; i++) {
  console.log(out);
}
