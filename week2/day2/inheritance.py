#INHERITANCE: PASSING ATTRIBUTES OR BEHAVIOR FROM A "FAMILY" MEMBER TO ANOTHER


#general concept of inheritance and syntax
class Parent:
    def speak(self):
        print('Parent is speaking')

class Child(Parent):
    def speak(self):
        print('Child is speaking')

class Grandchild(Child):
    pass

child1 = Child()
child1.speak()

grandchild = Grandchild()
grandchild.speak()

#inheriting attributes

class Animal:

    def __init__(self, name, family, legs):
        self.name = name
        self.family = family
        self.legs = legs

    def sleep(self):
        return f'{self.name} is sleeping - ANIMAL'
    
class Dog(Animal):
    
    def __init__(self, name, family, legs, trained, age):
        super().__init__(name, family, legs)
        self.trained = trained 
        self.age = age

class Cat(Animal):
    def __init__(self, name, family, legs, friendly, house_cat):
        super().__init__(name, family,legs)
        self.friendly = friendly
        self.house_cat = house_cat

#multiple inheritance
class Alien:

    def __init__(self, alien_name, planet):
        self.alien_name = alien_name
        self.planet = planet

class AlienDog(Alien, Dog): #the order matters 
    def __init__(self, alien_name, planet, name, family, legs, trained, age):
        Alien.__init__(self, alien_name, planet)
        Dog.__init__(self, name, family, legs, trained, age)



dog1 = Dog('Flufy', 'Canidae', 4, True, 5)
print(dog1.sleep())

#CREATE A CAT CLASS THAT INHERITS FROM ANIMAL ALL THE ANIMAL ATTRIBUTES + FRIENDLY AND HOUSE_CAT
#THEN CREATE AN OBJECT OF CAT AND PRINT IF IT IS FRIENDLY OR NOT

cat1 = Cat('Caramelo', 'Felidae', 4, True, True)
print(cat1.friendly)

aliendog1 = AlienDog('Chubi', 'Mars', 'Bob', 'Canidae', 6, True, 10 )
print(aliendog1.planet)