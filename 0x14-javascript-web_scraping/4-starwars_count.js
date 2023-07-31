#!/usr/bin/node
// prints title of a Star Wars movie where episode number matches a given integer
// Usage: ./4-starwars_count.js https://swapi-api.alx-tools.com/api/films/
const request = require('request');
const url = process.argv[2];

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const results = JSON.parse(body).results;// get list of movies
    console.log(results.reduce((count, movie) => {
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1// if condition true return increment
        : count;// else return initial vslue
    }, 0));// 0 is the initial vlue of count
  }
});
