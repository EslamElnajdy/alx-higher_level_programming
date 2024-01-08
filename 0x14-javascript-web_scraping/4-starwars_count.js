#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, res, body) => {
  if (error) {
    console.error(error);
  } else if (res.statusCode === 200) {
    const films = JSON.parse(body).results;
    const count = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)).length;
    console.log(count);
  }
});
