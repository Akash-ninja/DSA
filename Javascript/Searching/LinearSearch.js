/* user made */
function linearSearch(arr, key) {
  let elementPosition = -1

  arr.forEach((element, index) => {
    if (key === element) {
      elementPosition = index
    }
  })

  return elementPosition
}

const arr = [10, 34, 28, 182, 389, 192, 34]

const key = 34

// const foundIndex = linearSearch(arr, key)
// console.log(foundIndex)

/* Using JS built-in methods */
const discoveredIndex = arr.findIndex((element) => element === key)
console.log(discoveredIndex)

const observedIndex = arr.findLastIndex((element) => element === key)
console.log(observedIndex)
