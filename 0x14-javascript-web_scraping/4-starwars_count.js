#!/usr/bin/node
const request = require('request');

const URL = process.argv[2];

request(URL, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    const json = JSON.parse(body);
    const charFilms = json.results.filter(
      x => x.characters.find(y => y.match(/\/people\/18\/?$/))
    );
    console.log(charFilms.length);
  }
});
