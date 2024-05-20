export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter((student) => student.location === city).map((student) => {
    const updatedGrade = newGrades.find((grade) => grade.studentId === student.id);
    if (updatedGrade) {
      return { ...student, grade: updatedGrade.grade };
    }
    return { ...student, grade: 'N/A' };
  });
}
