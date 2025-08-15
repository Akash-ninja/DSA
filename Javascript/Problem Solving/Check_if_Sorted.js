/* Check if Array is sorted or not */

function isSorted(a = []) {
  for (let i = 0; i < a.length - 1; i++) {
    if (a[i] > a[i + 1]) return false
  }

  return true
}

const arr = [10, 2, 4, 6, 7]

console.log(isSorted(arr))
