class Animals():
    def __init__(self):
        self.ears = 2   # Private variable
        self.legs = 4    # Public variable
        self.living = True    #Protected Variable
        
    def setears(self, eyes):
        self.__ears = ears

    def getears(self):
        return self.__ears

    def getliving(self):
        return self._living

    def setliving(self, living):
        self._living = living

    def getlegs(self):
        return self.legs
    
    def setlegs(self, legs):
        self.legs = legs
        

# This class inherits all the methods of class animals        
class Tiger(Animals):

    def eats(self):
        print("A tiger eats meat!")


    def sound(self):
        print("A tiger roars!")

    def typeOfAnimal(self):
        print("Tiger is a carnivorous animal")
        
        
class Monkey(Animals):

    def eats(self):
        print("Monkey eats vegetables and fruits")


    def sound(self):
        print("A monkey makes a screeching sound!")

    def typeOfAnimal(self):
        print("LMonkey is a herbivorous animal")
        
class Dog(Animals):

    def eats(self):
        print("A dog eats meat, veggies, dog-food etc.!")

    def sound(self):
        print("A dog barks!")

    def typeOfAnimal(self):
        print("Dog is an omnivorous animal")
        
        
class Cat(Animals):

    def eats(self):
        print("A dog eats meat, veggies, cat-food etc.!")

    def sound(self):
        print("A dog meows!")

    def typeOfAnimal(self):
        print("A Cat is an omnivorous animal")

class Kangaroo(Animals):

    def eats(self):
        print("A Kangaroo eats vegetables, plants, leaves!")
   
    def sound(self):
        print("A Kangaroo growls or barks!")

    def typeOfAnimal(self):
        print("Kangaroo is a herbivorous animal")

class PolarBear(Animals):

    def eats(self):
        print("Polar Bear eats meat!")


    def sound(self):
        print("A polar bear makes sounds like hissing, growling or champing of teeth!")

    def typeOfAnimal(self):
        print("Polar Bear is a carnivorous animal")

class Deer(Animals):

    def eats(self):
        print("A deer eats plants, leaves!")


    def sound(self):
        print("A Deer makes a grunting sound or a bleating sound!")

    def typeOfAnimal(self):
        print("Deer is a herbivorous animal")

class Lion(Animals):

    def eats(self):
        print("Lion eats meat!")

    def sound(self):
        print("A lion roars!")

    def typeOfAnimal(self):
        print("Lion is a carnivorous animal")
        
class Giraffe(Animals):

    def eats(self):
        print("Giraffe eats leaves off the trees!")

    def sound(self):
        print("A giraffe makes a flute like sound!")

    def typeOfAnimal(self):
        print("Giraffe is a herbivorous animal")

class Zebra(Animals):

    def eats(self):
        print("Zebra eat grass!")


    def sound(self):
        print("Zebras either bark, bray or snort!")

    def typeOfAnimal(self):
        print("Zebra is a herbivorous animal")

