#!/usr/bin/node

let val = 0;
const max = Number(process.argv[2]);

if (max) {
  while (val < max) {
    console.log('C is fun');
    val++;
  }
} else {
  console.log('Missing number of occurrences');
}
