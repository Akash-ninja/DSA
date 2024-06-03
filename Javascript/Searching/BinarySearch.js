function IBinarySearch(arr, key) {
  let low = 0,
    high = arr.length - 1,
    mid = -1

  while (low <= high) {
    mid = Math.floor((low + high) / 2)

    if (key === arr[mid]) return mid
    else if (key < arr[mid]) high = mid - 1
    else low = mid + 1
  }

  return -1
}

/* Tail recursion used - can be coverted to iteration easily */
/* Since recursion uses stack so iteration is quite efficient here */
function RBinarySearch(arr, low, high, key) {
  if (low <= high) {
    let mid = Math.floor((low + high) / 2)

    if (key === arr[mid]) return mid
    else if (key < arr[mid]) return RBinarySearch(arr, low, mid - 1, key)
    else return RBinarySearch(arr, mid + 1, high, key)
  }

  return -1
}

const arr = [10, 20, 30, 40, 50, 60, 70, 80]

const key = 50

console.log("Element found at position: ", IBinarySearch(arr, key) + 1)

console.log(
  "Element found at position:",
  RBinarySearch(arr, 0, arr.length - 1, key) + 1
)
