#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(apiUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;
    const promises = data.map(character => {
      return new Promise((resolve, reject) => {
        request(character, (err, res, body2) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(body2).name);
          }
        });
      });
    });
    Promise.all(promises)
      .then(names => {
        names.forEach(name => console.log(name));
      })
      .catch(error => {
        console.error(error);
      });
  }
});
