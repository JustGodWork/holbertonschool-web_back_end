/* eslint-disable */
export default class HolbertonCourse {
  constructor(name, length, students) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() {
    return this._name;
  }

  set name(name) {
    if (typeof name === 'string') {
      this._name = name;
    } else {
      throw new Error('Name must be a string');
    }
  }

  get length() {
    return this._length;
  }

  set length(length) {
    if (typeof length === 'number') {
      this._length = length;
    } else {
      throw new Error('Length must be a number');
    }
  }

  get students() {
    return this._students;
  }

  set students(students) {
    if (Array.isArray(students)) {
      this._students = students;
    } else {
      throw new Error('Students must be an array');
    }
  }
}
