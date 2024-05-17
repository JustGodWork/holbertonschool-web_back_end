export default function guardrail(mathFunction) {
  let func;
  const queue = [];

  try {
    func = mathFunction();
  } catch (error) {
    func = error.toString();
  }
  queue.push(func);
  queue.push('Guardrail was processed');

  return queue;
}
