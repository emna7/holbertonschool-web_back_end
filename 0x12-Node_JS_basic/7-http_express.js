const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => res.send('Hello Holberton School!'));
app.get('/students', ((req, res) => {
  countStudents(String(process.argv.slice(2)))
    .then((arrayOfClasses) => {
      res.write('This is the list of our students\n');
      res.write(`Number of students: ${arrayOfClasses.count}\n`);
      for (const cls in arrayOfClasses) {
        if (cls && cls !== 'count') res.write(`Number of students in ${cls}: ${arrayOfClasses[cls].length}. List: ${arrayOfClasses[cls].join(', ')}\n`);
      }
      res.end();
    })
    .catch((err) => { throw err; });
}));
app.listen(1245);

module.exports = app;
