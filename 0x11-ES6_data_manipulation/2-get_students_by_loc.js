export default function getStudentsByLocation(studentsArray, city) {
  const arrayByCity = studentsArray.filter((student) => student.location === city);
  return arrayByCity;
}
