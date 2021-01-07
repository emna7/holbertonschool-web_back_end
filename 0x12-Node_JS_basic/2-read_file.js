const fs = require('fs');

const countStudents = (path) => {
  try {
    let data = fs.readFileSync(path, 'utf8').toString().split('\n');
    data = data.slice(1, data.length - 1);
    console.log(`Number of students: ${data.length}`);
    const arrayOfClasses = {};
    for (const row of data) {
      const student = row.split(',');
      if (!arrayOfClasses[student[3]]) arrayOfClasses[student[3]] = [];
      arrayOfClasses[student[3]].push(student[0]);
    }
    for (const cls in arrayOfClasses) {
      if (cls) console.log(`Number of students in ${cls}: ${arrayOfClasses[cls].length}. List: ${arrayOfClasses[cls].join(', ')}`);
    }
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};

module.exports = countStudents;
