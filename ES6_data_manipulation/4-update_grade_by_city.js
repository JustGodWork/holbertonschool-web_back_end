export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.map((student) => {
    if (student.location === city) {
      const updatedGrade = newGrades.find((grade) => grade.studentId === student.id);
      if (updatedGrade) return { ...student, grade: updatedGrade.grade };
    }
    return student;
  });
}
