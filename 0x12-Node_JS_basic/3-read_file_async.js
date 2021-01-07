const fs = require('fs');

const countStudents = (path) => {
  const promise = (res, rej) => {
    fs.readFile(path, (err, data) => {
      if (err) rej(Error('Cannot load the database'));
      if (data) {
        let dt = data.toString().split('\n');
        dt = dt.slice(1, dt.length - 1);
        console.log(`Number of students: ${dt.length}`);
        const arrayOfClasses = {};
        for (const row of dt) {
          const student = row.split(',');
          if (!arrayOfClasses[student[3]]) arrayOfClasses[student[3]] = [];
          arrayOfClasses[student[3]].push(student[0]);
        }
        for (const cls in arrayOfClasses) {
          if (cls) console.log(`Number of students in ${cls}: ${arrayOfClasses[cls].length}. List: ${arrayOfClasses[cls].join(', ')}`);
        }
      }
      res();
    });
  };
  return new Promise(promise);
};

module.exports = countStudents;
