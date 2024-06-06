/* Method:
1. Divide and Conquer procedure, Top-Down approach
 */

function Merge(arr, low, mid, high) {
  let i = (k = low),
    j = mid + 1,
    Aux = []

  // compare elements from partitioned array and copy them into another Auxiliary array
  while (i <= mid && j <= high) {
    if (arr[i] < arr[j]) {
      Aux[k++] = arr[i++]
    } else {
      Aux[k++] = arr[j++]
    }
  }

  // copy left over elements of arr to Aux
  while (i <= mid) {
    Aux[k++] = arr[i++]
  }

  while (j <= high) {
    Aux[k++] = arr[j++]
  }

  // copy down Aux array to return modified original array
  for (x in Aux) arr[x] = Aux[x]

  return arr
}

function MergeSort(arr, low, high) {
  if (low < high) {
    let mid = Math.floor((low + high) / 2)
    MergeSort(arr, low, mid)
    MergeSort(arr, mid + 1, high)
    Merge(arr, low, mid, high)
  }
  return arr
}

const arr = [200, 28, 10, 90, 56, 19, 100, 49, -2, 0]

const sortedArr = MergeSort(arr, 0, arr.length - 1)

console.log(sortedArr)
