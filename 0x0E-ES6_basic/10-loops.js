export default function appendToEachArrayValue(array, appendString) {
  const newArray = array;
  for (const val of array) {
    const idx = array.indexOf(val);
    newArray[idx] = appendString + val;
  }

  return newArray;
}
