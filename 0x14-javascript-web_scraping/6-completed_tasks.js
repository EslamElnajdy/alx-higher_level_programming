#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    body = JSON.parse(body);
    const result = {};
    for (let i = 0; i < body.length; i++) {
      if (body[i].completed === true) {
        if (result[body[i].userId] === undefined) {
          result[body[i].userId] = 1;
        } else {
          result[body[i].userId]++;
        }
      }
    }
    console.log(result);
  }
});
