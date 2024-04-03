#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi.dev/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Status:', response.statusCode);
  } else {
    const film = JSON.parse(body);
    const characters = film.characters;

    const characterNames = []; // Array to store character names

    // Function to request character data and store names
    const requestCharacter = (characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        } else if (response.statusCode !== 200) {
          console.error('Status:', response.statusCode);
        } else {
          const character = JSON.parse(body);
          characterNames.push(character.name); // Store character name
          if (characterNames.length === characters.length) {
            characterNames.forEach((name) => {
              console.log(name);
            });
          }
        }
      });
    };

    characters.forEach((characterUrl) => {
      requestCharacter(characterUrl);
    });
  }
});
