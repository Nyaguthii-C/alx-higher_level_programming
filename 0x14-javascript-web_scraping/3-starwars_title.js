#!/usr/bin/node
// prints title of a Star Wars movie where episode number matches a given integer
// Usage: ./100-starwars_characters.js <episode number>
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const episodeNum = process.argv[2];

request(url + episodeNum, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const response = JSON.parse(body);
    console.log(response.title);
  } else {
    console.log('Error ' + response.statusCode);
  }
});
