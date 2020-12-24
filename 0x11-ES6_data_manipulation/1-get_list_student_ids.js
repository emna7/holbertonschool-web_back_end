export default function getListStudentIds(objArrayStudents) {
  if (Array.isArray(objArrayStudents)) {
    return objArrayStudents.map((student) => student.id);
  }
  return [];
}
