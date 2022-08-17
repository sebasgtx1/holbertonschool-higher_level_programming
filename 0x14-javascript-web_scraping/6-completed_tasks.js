#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err == null) {
    const dict = {};
    const resp = JSON.parse(body);
    for (let i = 0; i < resp.length; i++) {
      if (resp[i].completed === true) {
        if (dict[resp[i].userId] === undefined) {
          dict[resp[i].userId] = 0;
        }
        dict[resp[i].userId]++;
      }
    }
    console.log(dict);
  }
});
