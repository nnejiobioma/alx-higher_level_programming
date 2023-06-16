#!/usr/bin/node

const val = process.argv[2];
const isNumber = !isNaN(val);

console.log(isNumber ? `My number: ${val}` : 'Not a number');
