/* Static properties and methods  */

class Cat {
  constructor(name) {
    this.name = name
  }

  // all instances of cats are the same species
  // so only one copy is created
  static genusSpecies = "Feline Catus"

  static meow() {
    return "MEOW MEOW MEOW!!"
  }

  // Static block - this will be invoked first
  static {
    const i = 0
    console.log("I am a static block")
  }

  describe() {
    return `${this.name} is a ${Cat.genusSpecies}`
  }
}

console.log(Cat.genusSpecies) // Feline Catus
console.log(Cat.meow()) // MEOW...
