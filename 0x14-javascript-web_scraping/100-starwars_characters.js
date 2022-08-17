#!/usr/bin/node
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err == null) {
    JSON.parse(body).characters.forEach(character => {
      request(character, function (err, response, body) {
        if (err == null) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
