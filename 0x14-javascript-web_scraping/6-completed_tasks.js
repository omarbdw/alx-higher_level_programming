#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
  } else {
    const tasks = JSON.parse(body);
    const completedTasks = {};

    tasks.forEach(function (task) {
      if (task.completed) {
        if (completedTasks[task.userId]) {
          completedTasks[task.userId]++;
        } else {
          completedTasks[task.userId] = 1;
        }
      }
    });

    for (const userId in completedTasks) {
      console.log(`${userId} : ${completedTasks[userId]}`);
    }
  }
});
