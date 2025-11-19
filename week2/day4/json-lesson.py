import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


#convert a python dictionary into a json file

my_family = {
    'parents':['Beth', 'Jerry'],
    'children': ['Summer', 'Morty']
}

with open(dir_path + '\my_family.json', 'w')  as f:
    json.dump(my_family, f)
    print('file was created')

#convert a python dictionary into a json string (short data)
my_family_json = json.dumps(my_family)
print(my_family_json)

#convert a json file into a python dictionary
with open(dir_path + '\my_family.json', 'r')  as f:
    my_family2 = json.load(f)

print(type(my_family2))

#convert a json string into a python dictionary
my_family3 = json.loads(my_family_json)
print(type(my_family3))