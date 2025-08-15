/* Remove duplicates (in-place) from Sorted Array */

function removeDuplicates(a = []) {
  let i = 0
  for (let j = 1; j < a.length; j++) {
    if (a[i] !== a[j]) {
      a[++i] = a[j]
    }
  }

  return i + 1
}

const nums = [1, 1, 2]

const iterations = removeDuplicates(nums)

for (let i = 0; i < iterations; i++) {
  console.log(nums[i])
}

/* Some notes: 
  1. Two pointers concept applied here - i and j are the pointers
  2. j will traverse the array and i will put the right element in its place */
