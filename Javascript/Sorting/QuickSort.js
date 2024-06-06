/* Method:
1. It selects first element to be pivot. (user dependent)
2. Sorting should be in such a way that elements before pivot is smaller and after is higher than the pivot element selected.
3. So, i moves from left to right direction when smaller element is found than pivot.
4. and, j moves from right to left direction when higher element is found than pivot.
5. Swapping is done when both i and j condition fails
 */

const swap = function (a, b) {
  return ([a, b] = [b, a])
}

function Partition(arr = [], low, high) {
  const pivot = arr[low]
  let i = low,
    j = high

  do {
    do {
      i++
    } while (arr[i] < pivot)
    do {
      j--
    } while (arr[j] > pivot)

    if (i < j) [arr[i], arr[j]] = swap(arr[i], arr[j])
  } while (i < j)
  ;[arr[low], arr[j]] = swap(pivot, arr[j]) // place the pivot element to j's position

  return j
}

function QuickSort(arr = [], low, high) {
  if (low < high) {
    const j = Partition(arr, low, high)
    QuickSort(arr, low, j)
    QuickSort(arr, j + 1, high)
  }
  return arr
}

const arr = [200, 28, 10, 90, 56, 19, 100, 49, -2, 0]

console.log(QuickSort(arr, 0, arr.length))
