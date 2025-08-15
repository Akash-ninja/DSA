/* Introduced in ES2022 - Static Initialization block */
class DatabaseConnection {
  static connection

  // static block
  static {
    console.log("Class is Loaded!")
  }
}

/* Another use-case of static method */
class Cat {
  constructor(name, breed) {
    this.name = name
    this.breed = breed
  }

  static registerStray() {
    const names = ["Muffin", "Biscuit", "Sleepy", "Dodo", "Princess Butterface"]

    const name = choice(names)
    return new Cat(name, "unknown")
  }

  meow() {
    return `${this.name} says meow`
  }
}

function choice(arr = []) {
  const randIdx = Math.floor(Math.random() * arr.length)
  return arr[randIdx]
}

console.log(Cat.registerStray())

const myCat = new Cat("Muffin", "feline catus")
console.log(myCat.meow())
