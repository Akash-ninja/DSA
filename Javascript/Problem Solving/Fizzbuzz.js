/* The famous Fizzbuzz problem which says that
    - print "fizz" if a number divides 3
    - print "buzz" if a number divides 5
    - print "Fizzbuzz" if a number divides 3 and 5 both*/

function fizzBuzz(num) {
  let output = ""

  if (num % 3 === 0) output += "Fizz"
  if (num % 5 === 0) output += "Buzz"
  if (output === "") output = num

  return output
}

for (let i = 1; i <= 100; i++) {
  console.log(fizzBuzz(i))
}

/* This approach provides 2 benefits
    Flexibility - Only have to change one place if number is different
    Scalability - can fit to any other set of numbers
 */
