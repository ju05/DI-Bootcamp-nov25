#CONDITIONALS

#LOGIC OPERATORS:
print(5 == '5') #equals
print(5 != '5') #different
print(5 < 3) #less than
print(5 <= 5) #less or equal than
print(5 > 2) #greater than

#syntax of conditional expression:

#if <condition>:
#    an indented block of code

client_age = int(input('What\'s your age?'))

if client_age <= 12:
    print('Sorry, you can\'t watch the movie')

if client_age < 7:
    print('We will call your parents')

elif client_age >= 13 and client_age <= 16:
    print('You can watch the movie with your parents')

elif client_age > 16:
    print('You can watch the movie')
