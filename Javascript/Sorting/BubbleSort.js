const swap1 = function (a, b) {
  return ([a, b] = [b, a])
}

const swap2 = function (a, b) {
  let temp = a
  a = b
  b = temp

  return [a, b]
}

const swap3 = function (a, b) {
  a = a + b
  b = a - b
  a = a - b

  return [a, b]
}

const swap4 = function (a, b) {
  a = a ^ b
  b = a ^ b
  a = a ^ b

  return [a, b]
}

function BubbleSort(arr = []) {
  let flag

  /* number of passes */
  for (let i = 0; i < arr.length; i++) {
    flag = 0

    /* comparison and swaps */
    for (let j = 0; j < arr.length - i - 1; j++) {
      if (arr[j] > arr[j + 1]) {
        ;[arr[j], arr[j + 1]] = swap1(arr[j], arr[j + 1])
        flag = 1
      }
    }

    /*  makes algorithm adaptive - dont check for comparison if array is already sorted */
    if (!flag) return arr
  }

  return arr
}

const arr = [129, 28, 10, 90, 56, 19, 100, 49, -2, 0]

console.log(BubbleSort(arr))
