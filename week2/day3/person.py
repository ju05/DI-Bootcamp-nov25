#DECORATORS

import re #module for regex expressions (you can find patterns to help to clean strings (delete special chars or digits, etc))
import datetime

class Person:

    def __init__(self, first_name, last_name, birth_date):
        self.first_name = self.format_name(first_name) #before the string caming from the argument is added to the internal dict of the object, we format it.
        self.last_name = self.format_name(last_name)
        self.birth_date = birth_date    
        self._email = f'{self.first_name}.{self.last_name[0]}@mycompany.com'.lower() #protected attribute
        self.__salary = 30000 #private attribute

    @classmethod #a method that uses the class instance to create an object in a different way (different arguments)
    def from_age(cls, first_name, last_name, age):
        current_year = datetime.datetime.today().year
        birth_year = current_year - age
        birth_date = f'1-1-{birth_year}'
        return cls(first_name, last_name, birth_date)
    
    @property
    def age(self):
        today = datetime.datetime.today()
        age = today.year - self.parse_bithdate().year
        return age
    
    @property #getter
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email.lower()

    @staticmethod #a method without self - usually used for internal formating
    def format_name(name):
        name = name.strip().capitalize()
        name = re.sub(r'[^a-zA-Z]', '', name)
        return name
    
    def presentation(self):
        print(f'Hello, my name is {self.first_name}')
    
    def parse_bithdate(self):
        return datetime.datetime.strptime(self.birth_date, '%d-%m-%Y')


    #DUNDER METHODS AKA MAGIC METHODS

    def __str__(self): #prints this string when we print the object 
        return f'Hello, my name is {self.full_name}, my birth-date is {self.birth_date}'
    
    def __repr__(self):#prints a string with internal information (like the properties of an object, for example)
        return f'{self.__dict__}'
    
    def __eq__(self, other): #checks if two objects have some equal value (can be any property/attribute)
        return len(self.first_name) == len(other.first_name)


p1 = Person('john', 'snow&', '05-12-1980')
p2 = Person('ARIA', ' STARK5', '30-07-2000')
# print(p1.first_name, p1.last_name) #because we have the format_name on the init, the first_name and last_name are formated with Capital letters
# print(p2.first_name, p2.last_name)

p1.first_name = 'Maria'
print(p1.presentation())

# print(p1)
print(p1.age)
print(p1.email)
p1.email = 'the.choosen@mycompany.com'
print(p1.email)

# print(p1.__salary) #gives AttributeError
#a work around that can give you access to a private attribute:
print(p2._Person__salary)

#creating an object using our classmethod 
p3 = Person.from_age('Sansa', 'stark', 30)
print(p3.birth_date)
print(p1 == p2)

#CREATE A STATICMETHOD THAT FORMAT THE FIRST_NAME AND LAST_NAME AS FULL_NAME.
#CREATE AN INTERNAL ATTRIBUTE CALLED FULL_NAME AND DO IT WITH THE STATIC METHOD
#CREATE p4 NAME Daenerys Targaryen AGE 32
#PRINT DAENERYS FULL_NAME

