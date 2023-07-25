#!/usr/bin/node

const fs = require('fs');

const data = process.argv[2];

fs.writeFile(process.argv[3], data, 'utf8', (error) => {
  if (error) console.log(error);
});

