#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, _res, body) {
  if (err) {
    console.log(err);
  } else {
    const compbyusr = {};
    body = JSON.parse(body);

    for (let i = 0; i < body.length; ++i) {
      const userId = body[i].userId;
      const comp = body[i].comp;

      if (comp && !compbyusr[userId]) {
        compbyusr[userId] = 0;
      }

      if (comp) ++compbyusr[userId];
    }

    console.log(compbyusr);
  }
});
