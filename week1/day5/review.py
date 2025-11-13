#DAY 1 - NO NEED FOR REVIEW
#DAY 2

#LIST = Mutable, ordered sequence 

friends = ['Ross', 'Rachel', 'Monica', 'Joey', 'Chandler', 'Phoebe']

print(friends[2])
print(friends[2:5]) #slicing 

#list methods
friends.append('Juliana')
friends.insert(2, 'Juliana')
friends.remove('Monica')
del friends[2]
poped_value = friends.pop()

print(f'bye bye {poped_value}')
print(friends)

#sorted()
# print(friends)
# sorted_friends = sorted(friends)
# print(sorted_friends)

#sort()
print(friends)
friends.sort()
print(friends)

#split() - creates a list as output
# user_info = input('enter your name and age separated by comma: ').split(',')
# print(user_info)

# ages = input('enter the ages of the family member separated by space').split()
# print(ages)

#join() is a str methid that needs a sequence as argument
# students = input('enter the students names').split()

# print(f'The news students are: {', '.join(students)}')


# #LOOPS

# # FOR LOOP
# #syntax:
# #for <variable> in <sequence>:
# #   an indented block of code

# for student_name in students:
#     print(f'Welcome, {student_name}')

#Create a list containing the following sequence of mixed types: floats and integers:
# 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5

output = []
for num in range(1,6):
    output.append(num)
    output.append(num + 0.5)

print(output[1:-1])

#WHILE
# Write a loop that asks the user to enter pizza toppings one by one.
# Stop the loop when the user types 'quit'.
# For each topping entered, print:
# "Adding [topping] to your pizza."
# After exiting the loop, print all the toppings and the total cost of the pizza.
# The base price is $10, and each topping adds $2.50.


toppings_list = []
price = 10

while True:
    topping = input('enter the topings or "q" for quit').lower()
    
    if topping == 'q':
        if toppings_list:
            print(f'Your toppings are: {', '.join(toppings_list)} and the price is {price}')
            break
        else:
            print(f'You didn\'t choose any toipping, the price is {price}')
            break
    else:
        toppings_list.append(topping)
        price += 2.50
        print(f'the {topping} was added to your pizza')

    
    
