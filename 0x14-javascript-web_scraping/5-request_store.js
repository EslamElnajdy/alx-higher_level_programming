#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filename = process.argv[3];
request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else if (res.statusCode === 200) {
    fs.writeFile(filename, body, 'utf-8', (error) => {
      console.log(error);
    });
  }
});
