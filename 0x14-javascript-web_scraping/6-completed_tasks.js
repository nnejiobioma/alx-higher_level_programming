#!/usr/bin/node

const requestURL = process.argv[2];
const request = require('request');
const usersId = {};

request(requestURL, function (error, response, body) {
  if (error) {
    return console.log(error);
  }

  const base = JSON.parse(body);

  for (let i = 0; i < base.length; i++) {
    const item = base[i].userId;
    if (base[i].completed) {
      usersId[item] = (usersId[item] || 0) + 1;
    }
  }

  console.log(usersId);
});
