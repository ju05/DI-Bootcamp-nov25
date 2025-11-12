#DICTIONARIES: COMPLEX DATA STRUCTURE

student_info1 = ['Harry', 'Potter', 15, 'Privet Drive, 4', 'Hedwig', 'Buckbeak']

student_info = {'first_name':'Harry',
                'last_name': 'Potter',
                'age':15,
                'address':'Privet Drive, 4',
                'pets':['Hedwig', 'Buckbeak'],
                'best_friends': ('Ron Wealey', 'Hermione Granger'),
                'is_parselmouth': True,
                'houses': {'main': 'Griffyndor', 'second': 'Slytherin'}}


#accessing data
print(student_info['first_name'])
student_info['pets'][1]
print(student_info)
print(student_info['houses']['main'])

#how to use methods on dictionary values
student_info['pets'].append('Toby')
print(student_info['first_name'].upper())

#changing values of a dictionary
student_info1[0] = 'Tiago'
student_info['first_name'] = 'Tiago'

print(student_info['first_name'])

#how to add a new key:value pair
student_info['teachers'] = 'Snap' #option1
student_info.update({'principal':'Dumbleadore'}) #option2

print(student_info)

del student_info['address']
print(student_info)


#EXERCISE:
#print Harry's age
#add 10year to it and print again
student_info['age'] += 10
print(student_info['age'])

#change the address to "Betzalel 8"
student_info['address'] = 'Betzalel 8'
print(student_info['address'])

#add a new pet to the pets list
student_info['pets'].append('Miau')
#change the is_parselmouth to False
student_info['is_parselmouth'] = False

#Exercise
sample_dict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

print(sample_dict['class']['student']['marks']['history'])

#set vs dictionary
# my_set = {'Israel', 'US', 'Brazil'}
# my_dict = {'name': 'Juliana'}
# print(type(my_set))
# print(type(my_dict))





