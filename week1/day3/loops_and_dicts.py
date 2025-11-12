#LOOPS AND DICTIONARIES

student_info1 = ['Harry', 'Potter', 15, 'Privet Drive, 4', 'Hedwig', 'Buckbeak']

student_info = {'first_name':'Harry',
                'last_name': 'Potter',
                'age':15,
                'address':'Privet Drive, 4',
                'pets':['Hedwig', 'Buckbeak'],
                'best_friends': ('Ron Wealey', 'Hermione Granger'),
                'is_parselmouth': True,
                'houses': {'main': 'Griffyndor', 'second': 'Slytherin'}}

#loop in a list = directly
# for item in student_info1:
#     print(item)

#options of loops in dictionaries:

# #access only keys = keys()
# for key in student_info.keys():
#     print(key)

# #access only keys = values()
# for value in student_info.values():
#     print(value)

#access both: keys and values
# for key, value in student_info.items():
#     print(key, value)

#we want to change all the string values to upper case
for key, value in student_info.items(): #accessing both: keys and values
    if type(value) == str: #check if the value is a string
        student_info[key] = value.upper() #changing the value to UPPERCASE

print(student_info)

