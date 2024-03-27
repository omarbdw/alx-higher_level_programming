#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const todos = JSON.parse(body);
    const completedTasks = {};

    todos.forEach(function (todo) {
      if (todo.completed) {
        if (completedTasks[todo.userId]) {
          completedTasks[todo.userId]++;
        } else {
          completedTasks[todo.userId] = 1;
        }
      }
    });
    const dict = {};
    for (const userId in completedTasks) {
      if (completedTasks[userId] !== 0) {
        dict[userId] = completedTasks[userId];
      }
    }
    console.log(dict);
  }
});
