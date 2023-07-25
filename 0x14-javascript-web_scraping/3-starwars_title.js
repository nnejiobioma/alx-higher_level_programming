#!/usr/bin/node

const starWarsUri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);
const request = require('request');

request(starWarsUri, function (_error, _response, body) {
    console.log(body.title);
    body = JSON.parse(body);
});
