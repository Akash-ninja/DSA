/* Method:
1. It selects a position and searches for the right element in that place.
2. By this way, it gets the smallest element at first and then smaller ones.
3. i => position where right element to be inserted, 
   j => moving pointer for comparisons
   k => points to the place of smallest element.
*/

const swap1 = function (a, b) {
  return ([a, b] = [b, a])
}

function SelectionSort(arr = []) {
  let i, j, k
  for (i = 0; i < arr.length; i++) {
    for (k = j = i; j < arr.length; j++) {
      if (arr[j] < arr[k]) {
        k = j
      }
    }
    ;[arr[i], arr[k]] = swap1(arr[i], arr[k])
  }

  return arr
}

const arr = [129, 28, 10, 90, 56, 19, 100, 49, -2, 0]

console.log(SelectionSort(arr))

// pass1: arr = [-2, 28, 10, 90, 56, 19, 100, 49, 129, 0]
// pass2: arr = [-2, 0, 10, 90, 56, 19, 100, 49, 129, 28]
// pass3: arr = [-2, 0, 10, 90, 56, 19, 100, 49, 129, 28]
// pass4: arr = [-2, 0, 10, 19, 56, 90, 100, 49, 129, 0]...
