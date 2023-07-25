#!/usr/bin/node

const fs = require('fs');

function readFileContent(err, data) {
  if (err) {
    return console.log(err);
  }
  process.stdout.write(data);
}

if (process.argv.length < 3) {
  console.log("Usage: node script_name.js file_path");
  process.exit(1);
}

const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', readFileContent);

