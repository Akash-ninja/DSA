/* Method:
1. It assumes the first element is already sorted
2. Moving pointer for comparison (j) moves decrementally from i's prev position
3. Element is selected and searched for its right place for that pass
4. Insertion takes place by shifting elements to the right
 */

/* sort kind of playing cards */
function InsertionSort(arr = []) {
  for (let i = 1; i < arr.length; i++) {
    j = i - 1
    let x = arr[i]

    while (j > -1 && arr[j] > x) {
      arr[j + 1] = arr[j]
      j--
    }

    arr[j + 1] = x
  }

  return arr
}

const arr = [129, 28, 10, 90, 56, 19, 100, 49, -2, 0]

console.log(InsertionSort(arr))

// pass1 = [28, 129, 10, 90, 56, 19, 100, 49, -2, 0]
// pass2 = [10, 28, 129, 90, 56, 19, 100, 49, -2, 0]
// pass3 = [10, 28, 129, 90, 56, 19, 100, 49, -2, 0] //same as pass2 because arr[j] > x
// pass4 = [10, 28, 56, 129, 90, 19, 100, 49, -2, 0]...
