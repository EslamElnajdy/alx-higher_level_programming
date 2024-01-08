#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    for (let i = 0; i < data.length; i++) {
      request(data[i], (err, res, body2) => {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body2).name);
        }
      });
    }
  }
});
