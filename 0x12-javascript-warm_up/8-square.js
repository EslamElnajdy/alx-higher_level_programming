#!/usr/bin/node
const arg = process.argv.slice(2);
let num = parseInt(arg, 10);
let out = 'X';
if (isNaN(num)) {
  out = 'Missing size';
  num = 1;
}
for (let i = 0; i < num; i++) {
  let row = '';
  for (let j = 0; j < num; j++) {
    row += out;
  }
  console.log(row);
}
