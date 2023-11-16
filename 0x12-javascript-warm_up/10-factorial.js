#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);
function factorial (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a > 1) {
    return a * (factorial(a - 1));
  } else {
    return a;
  }
}
console.log(factorial(num));
