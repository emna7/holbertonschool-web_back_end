export default function getStudentIdsSum(studentsArray) {
  const reducer = (accumulator, currentValue) => accumulator + currentValue.id;
  const idSum = studentsArray.reduce(reducer, 0);
  return idSum;
}
