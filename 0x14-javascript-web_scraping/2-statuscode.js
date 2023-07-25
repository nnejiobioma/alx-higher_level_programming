#!/usr/bin/node

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (error, response, body) {
  if (error) {
    return console.log(error);
  }
  console.log('code: ' + response.statusCode);
});
