#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];
let count = 0;
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const movies = JSON.parse(body).results;
    for (const movie of movies) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
