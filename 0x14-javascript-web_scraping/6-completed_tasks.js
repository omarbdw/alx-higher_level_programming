#!/usr/bin/node
const request = require('request');

const apiUrl = 'https://jsonplaceholder.typicode.com/todos';

request(apiUrl, (error, response, body) => {
	if (error) {
		console.error('Error:', error);
	} else if (response.statusCode !== 200) {
		console.error('Status:', response.statusCode);
	} else {
		const tasks = JSON.parse(body);
		const completedTasksByUser = {};

		tasks.forEach(task => {
			if (task.completed) {
				if (completedTasksByUser[task.userId]) {
					completedTasksByUser[task.userId]++;
				} else {
					completedTasksByUser[task.userId] = 1;
				}
			}
		});

		Object.keys(completedTasksByUser).forEach(userId => {
			console.log(`User ${userId} completed ${completedTasksByUser[userId]} tasks`);
		});
	}
});
