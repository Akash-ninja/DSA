class Cat {
  // Public fields: provides documentation for the class
  static numOfCats = 0
  name
  breed
  numLegs = 4
  hasTail = true

  constructor(name, breed) {
    this.name = name
    this.breed = breed
    Cat.numOfCats += 1
  }

  amputate() {
    this.numLegs -= 1
  }
}

class Circle {
  // Private field
  #radius
  constructor(radius) {
    this.#radius = radius
  }

  // Private method
  #getCircleDiameter() {
    console.log("Cannot be called outside class")
    return this.#radius * 2
  }

  // Public method
  getDiameter() {
    return this.#getCircleDiameter()
  }

  getRadius() {
    return this.#radius
  }
}

const myCircle = new Circle(10)
console.log(myCircle.getRadius())
// myCircle.#radius -> Error

console.log(myCircle.getDiameter())
