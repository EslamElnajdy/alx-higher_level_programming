#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, res, body) => {
  if (error) {
    console.error(error);
  } else if (res.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < films.length; i++) {
      for (let j = 0; j < films[i].characters.length; j++) {
        if (films[i].characters[j].includes('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
