export default function updateStudentGradeByCity(studentsArray, city, newGradesArray) {
  const studentsByCity = studentsArray.filter((stud) => stud.location === city);
  return studentsByCity.map((stud) => {
    const student = stud;
    const studGrade = newGradesArray.filter((grade) => grade.studentId === stud.id);
    if (studGrade.length !== 0) student.grade = studGrade[0].grade;
    else student.grade = 'N/A';
    return stud;
  });
}
