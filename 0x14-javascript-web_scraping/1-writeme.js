#!/usr/bin/node
const process = require('process');
const fs = require('fs');

const cont = process.argv[2];

const text = process.argv[3];

fs.writeFile(cont, text, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
