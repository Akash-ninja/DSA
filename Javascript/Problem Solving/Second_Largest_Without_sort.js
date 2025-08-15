/* Return second smallest and largest without sorting */

function secondLargest(a = []) {
  let max = a[0],
    secondMax = -1

  for (let i = 1; i < a.length; i++) {
    if (a[i] > max) {
      secondMax = max
      max = a[i]
    } else if (a[i] < max && a[i] > secondMax) {
      secondMax = a[i]
    }
  }

  return secondMax
}

function secondSmallest(a = []) {
  let min = a[0]
  secondMin = Number.MAX_SAFE_INTEGER

  for (let i = 1; i < a.length; i++) {
    if (a[i] < min) {
      secondMin = min
      min = a[i]
    } else if (a[i] != min && a[i] < secondMin) {
      secondMin = a[i]
    }
  }

  return secondMin
}

// const arr = [10, 5, 10]
const arr = [129, 28, 10, 90, 56, 19, 100, 49, 93, 0]

const secondLargestNum = secondLargest(arr)
const secondSmallestNum = secondSmallest(arr)

console.log(secondLargestNum, secondSmallestNum)
