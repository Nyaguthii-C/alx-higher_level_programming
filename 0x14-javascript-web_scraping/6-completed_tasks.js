#!/usr/bin/node
// get users who have ecompleted tasks
// and number of tasks completed
// print an object containing user IDs as keys
// and the corresponding count of completed todos as values
// API: https://jsonplaceholder.typicode.com/todos

const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const DoneTasks = {};// store the counts of completed todos for each user
    const todos = JSON.parse(body);

    for (const user in todos) {
      const todo = todos[user];// individual tasks
      if (todo.completed === true) { // for each task that is completed
        if (DoneTasks[todo.userId] === undefined) { // 1st of user done task
          DoneTasks[todo.userId] = 1;// start count
        } else {
          DoneTasks[todo.userId]++;// if previously encounteered, increment
        }
      }
    }
    console.log(DoneTasks);
  }
});
