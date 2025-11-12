#BASIC DATA TYPES

#STRING (str):IS TEXT IN PYTHON, WRITEN IN BETWEEN QUOATATION MARKS, A SEQUENCE OF CHARS
#STRING METHODS
#upper()
#lower()
#replace()

#NUMBERS: INTEGERS (int), FLOATS (floats), COMPLEX

#CASTING TYPES

#BOOLEANS (bool): True/False values 

#NoneType: nothing. None 

#YOU DO NOW:
# >>> type(1234) int
# >>> type(5.5) float
# >>> type(3.153) float
# >>> type(True) bool
# >>> type(False) bool
# >>> type('Python') str

# my_name = 'Juliana'
# name_upper = my_name.upper()

# print(name_upper)

# #STRING ARE IMMUTABLE

# # my_name[0] = 'G'
# print(my_name)

# #SPECIAL CHARS IN STRINGS
# sentence = 'I love Python\n'
# print(sentence * 3)

# sentence = 'I love Python\t'
# print(sentence * 3)

# sentence = 'I\'m in love with Python'
# print(sentence * 3)


# sentence_js = sentence.replace('Python', 'JavaScript')
# print(sentence_js)

# price = '15$'

# clean_price = int(price.replace('$', ''))
# print(type(clean_price))

# description = "strings are sequence of characters"
# print(description.upper())
# print(description.replace('are', 'is'))

# #STRING SLICING
# print(description[:7])

# #Variables

# f_name = 'Harry'
# l_name = 'Potter'
# age = 15
# address = 'Privet Drive 4'
# is_wizzard = True

# #HOW TO NAME THEM: BEST PRACTICES
# # DON'T START WITH NUMBERS OR SPECIAL CHARS(EXAMPLE OF NOT GOOD: 14 = 'MY FAVORITE NUMBER'
# # USE: SHORT NAMES, IN PYTHON BETTER TO USE UNDERSCORE AS SPACE

# first_name = 'Ron'
# print(5 == 3)

# #the variable doesn't store the expression, but the output of the expression
# calculation = 5+6
# print(calculation)

# general_var = 'Hello'
# general_var = 456
# general_var = True
# print(general_var)

x = 1
y = 2

#try to swap the values of x and y
# temp = y
# y = x
# x = temp
# print(x, y)

x,y = y,x
print(x,y)

# #useful functions: 
# #print() - it shows something defined on the bracksts on the terminal
# #input()- prompt the user for some input

# user_name = input('Enter your name: ') #the inputed info comes as a str
# print(user_name)
# age = int(input('enter your age:'))
# print(age + 10)

# print(f'{user_name} is {age} years old')

# #f` strings = the f` stand for format()`

# #Increment a variable
# count = 0
# user_name = input('Enter your name: ')
# count += 1
# print(user_name)
# print(count)

# output = ''

# output += 'J'
# output += 'U'
# print(output)

#Exercise
# user_age = int(input('What\'s your age?'))
# print(f'You will turn 100 in {100 - user_age} years')

