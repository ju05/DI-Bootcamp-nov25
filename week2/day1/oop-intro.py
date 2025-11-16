#OOP - OBJECT ORIENTED PROGRAMING

#HOW TO CREATE A CLASS OF OBJECTS

class Dog:
    def __init__(self, name, color, breed, age, is_trained = True): #the constructor function 
        self.name = name
        self.color = color
        self.breed = breed
        self.age = age
        self.is_trained = is_trained

    def bark(self): #function > method
        print(f'{self.name} goes Woof Woof\n'*self.age)

    def run(self):
        if self.age > 5:
            print(f'{self.name} prefers to walk.')
        else:
            print(f"{self.name} is running.")

    def walk(self, person):
        print(f'{person} is walking {self.name}')

    def rename(self, new_name):
        self.name = new_name
        return self   

    

#create a method called run() that checkes the dog's age and if the dog is older than 5 you print "dog.name" prefers to walk. else you print c  
# then call the method on dog2 

#HOW TO CREATE AN OBJECT OF A SPECIFIC CLASS
dog1 = Dog('Rex', 'black', 'german shepherd', 8, True)
print(dog1)

#accessing the attributes of a dog:
print(dog1.name)
print(dog1.age)
print(dog1.is_trained)
print(dog1.__dict__)

dog1.guidance_dog = True
print(dog1.guidance_dog)

#create a second object of class Dog, call it dog2 and you choose the attributes
dog2 = Dog('Muchtar', 'grey', 'german shepherd', 1, False)
print(dog2.age)
print(dog2.__dict__)

#CALL THE METHOD: in order to call a method we need to use the object
dog1.bark()
dog2.bark()

dog1.run()
dog2.run()

dog2.walk('John')
dog2.rename('Toto')
print(dog2.name)
print(dog2.__dict__)

# create a class called BankAccount, with 3 attributes:
#- account houlder = name + last name of a person
#- account number = random number
#- balance which starts with 50.00 (float)