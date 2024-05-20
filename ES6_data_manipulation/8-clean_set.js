export default function cleanSet(set, startString) {
  if (typeof startString !== 'string') return '';

  const arrayValues = Array.from(set).filter((value) => value.startsWith(startString));
  const values = arrayValues.map((value) => {
    if (value.startsWith(startString)) return value.replace(new RegExp(`^${startString}`), '');
    return value;
  });

  return values.join('-');
}
