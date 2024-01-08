#!/usr/bin/node

const request = require('request');

const id = process.argv[2];
const urlApi = `https://swapi-api.alx-tools.com/api/films/${id}`;
request(urlApi, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
