import os

#Python - I/O

#OLD SCHOOL WAY: YOU NEEDED TO EXPLICITY CLOSE THE FILE AFETER USING IT - USING CLOSE() METHOD

# file_obj = open('file-name.txt', 'w')
# your code to do anything you want
# file_obj.close()

#NEW WAY: USE WITH STATEMENT

# with open('secrets.txt', 'r') as file_obj: #FileNotFoundError: [Errno 2] No such file or directory: 'secrets.txt'
#     print(file_obj.read())

#solution for the FileNotFoundError = use os module to give the full path to the file
dir_path = os.path.dirname(os.path.realpath(__file__))

with open(dir_path + '\secrets.txt', 'r') as file_obj: #FileNotFoundError: [Errno 2] No such file or directory: 'secrets.txt'
    content = file_obj.read()
    print(content)



#exercise
with open(dir_path + '\starwars.txt', 'r') as f:
    #use the method to read line by line
    txt_list = f.readlines()
    for line in txt_list:
        print(line)
    print('end of document')

# Read only the 5th line of the file
    # print(txt_list[4])

# Read only the 5 first star wars characters of the file
    # print(txt_list[:5])

# Read all the file and return it as a list of strings. Then split each word into letters
    # temp = [] #step1
    # for name in txt_list: #step 2
    #     temp.append(list(name)) #step3

    # print(temp)

    #list comprehension
    temp = [list(name) for name in txt_list]
    print(temp)


# Find out how many occurences of the names "Darth", "Luke" and "Lea" are in the file
    # counts = {'Darth': 0, 'Luke': 0, 'Lea':0}
    # for name in txt_list:
    #     if name == 'Darth':
    #         counts['Darth'] += 1
    #     elif name == 'Luke':
    #         counts['Luke'] += 1
    #     elif name == 'Lea':
    #         counts['Lea'] += 1    
    # print(counts)

    #### BUT THERE IS A BETTER WAY: USE count()

    full_txt_str = ''.join(txt_list)

    counts = {'Darth': full_txt_str.count('Darth'),
              'Luke': full_txt_str.count('Luke'),
              'Lea': full_txt_str.count('Lea')

    }

    print(counts)

# Append your first name at the end of the file
# with open(dir_path + '\starwars.txt', 'a+') as f:
#     f.seek(0, os.SEEK_END)
#     f.write('\nJuliana')
#     print('sucessfully added')

# Write "SkyWalker" next to each first name "Luke"
with open(dir_path + '\starwars.txt', 'r+') as f:
    txt_list = f.readlines()
    modified_content = []
    for name in txt_list:
        if name == 'Luke\n':
            modified_content.append('Luke Skywalker\n')
        else:
            modified_content.append(name)
    print(modified_content)
    
with open(dir_path + '\starwars.txt', 'w') as f:
    f.seek(0)
    f.writelines(modified_content)
    print('Skywalker was added')