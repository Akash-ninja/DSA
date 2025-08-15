/* Class, constructor, Inheritance in javascript */

class Triangle {
  constructor(a, b) {
    if (!Number.isFinite(a) || a <= 0) throw new Error(`Invalid a: ${b}`)
    if (!Number.isFinite(b) || b <= 0) throw new Error(`Invalid b: ${b}`)

    this.a = a
    this.b = b
  }

  // Getter
  get oneSide() {
    return this.a
  }

  // Setter
  set otherSide(value) {
    if (value < 0) throw new Error("Side of a triangle cannot be negative")
    else this.b = value
  }

  // Instance method
  getArea() {
    return (this.a * this.b) / 2
  }

  getHypotenuse() {
    return Math.sqrt(this.a ** 2 + this.b ** 2)
  }

  sayHi() {
    return `The triangle with side A of ${this.a} and side B of ${
      this.b
    } and with an area of ${this.getArea()} says HI!!!`
  }

  describe() {
    return `Area is ${this.getArea()}.`
  }
}

class ColorTriangle extends Triangle {
  constructor(a, b, color) {
    super(a, b) // calls the parent or super-class constructor
    this.color = color
  }

  describe() {
    return `Area is ${this.getArea()}.` + ` Color is ${this.color}`
  }
}

class ColorMoodTriangle extends ColorTriangle {
  constructor(a, b, color, mood) {
    super(a, b, color)
    this.mood = mood
  }
}

// Object instantiation
const regularTri = new Triangle(3, 5)
console.log(regularTri.sayHi())

const colorMoodTri = new ColorMoodTriangle(4, 6, "Green", "Happy")
console.log(colorMoodTri.describe()) // if method not present in that class, then calls the parent-class method

console.log(regularTri.oneSide)
regularTri.otherSide = 9
console.log(regularTri.getArea())
