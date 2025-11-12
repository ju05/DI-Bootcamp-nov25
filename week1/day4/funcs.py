#FUNCTIONS

#syntax of a function:

#def <name_of_function>(empty/<arguments>):
#   an indented block of code

#call the function by the name of it

# def greetings():
#     print('Welcome, user!')

# greetings()

# #arguments in functions
# def greetings(user_name):
#     print(f'Welcome, {user_name}!')

# greetings('Gandalf')

# #default arguments 
# def greetings(user_name = 'John Doe'):
#     print(f'Welcome, {user_name}!')

# greetings('Frodo')

#positional argument = the position that you enter the argument, matters
# def greetings(user_name, language = 'EN'):
#     language == 'EN'
#     print(f'Welcome, {user_name}!')
#     if language == 'PT':
#         print(f'Bem-vindo, {user_name}!')
#     elif language == 'IT':
#         print(f'Benvenuto, {user_name}!')
#     elif language == 'RU':
#         print(f'Privet, {user_name}')

# greetings('Aragorn', 'JP')

#keyword arguments
def greetings(user_name, language = 'EN'):
    
    if language == 'PT':
        print(f'Bem-vindo, {user_name}!')
    elif language == 'IT':
        print(f'Benvenuto, {user_name}!')
    elif language == 'RU':
        print(f'Privet, {user_name}')
    else:
        print(f'Welcome, {user_name}!')


greetings(language = 'JP', user_name = 'Aragorn')

#mixed (keyword + positional argument)= the keyword argument must be before the positional argument

def greetings(user_name, language = 'EN'):
    language == 'EN'
    print(f'Welcome, {user_name}!')
    if language == 'PT':
        print(f'Bem-vindo, {user_name}!')
    elif language == 'IT':
        print(f'Benvenuto, {user_name}!')
    elif language == 'RU':
        print(f'Privet, {user_name}')

greetings('Aragorn',language = 'RU')

# create a function called country_info that receives a country name as argument
# and prints the capital of that country. Make the country name argument default
# Naboo (star wars planet). Its capital is Theed


def country_info(country = 'Naboo'):
    if country == 'Russia':
        capital = 'Moscow'

    elif country == 'USA':
        capital = 'Washington DC'

    elif country == 'Brazil':
        capital = 'Brasilia' 

    elif country == 'Naboo':
        capital = 'Theed'  

    return capital

print(country_info('Brazil'))

def sum_numbers(x, y):
    result = x + y
    return result

def multiply(j):
    multiplier = sum_numbers(3, 2)
    result = j * multiplier
    return result

print(multiply(4))

#using the return keyword
