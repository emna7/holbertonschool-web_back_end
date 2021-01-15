module.exports = function calculateNumber(a, b) {
  const numA = Number(a);
  const numB = Number(b);
  if (Number.isNaN(numA) || Number.isNaN(numB))
  throw TypeError;

  return (Math.round(numA) + Math.round(numB));
}
