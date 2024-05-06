/**
 * Create a constant named task and return it
 * @returns {string} task
 */
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

/**
 * Create an anonymous string and return it
 * @returns {string} task
 */
export function getLast() {
  return ' is okay';
}

/**
 * Create an editable string and return it
 * @returns {string} task
 */
export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
