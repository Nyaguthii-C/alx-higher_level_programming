#!/usr/bin/node
// display the status code of a GET request
const request = require('request');
const url = process.argv[2];

request(url, (error, response) => {
  // Printing the error if occurred
  if (error) console.log(error);

  // Printing status code
  const code = response.statusCode;
  console.log(`code: ${code}`);
});
