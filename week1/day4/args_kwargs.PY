#*ARGS AND **KWARGS (JUST ARGUMENTS, KEY WORD ARGUMENT)

friends = ['Ross', 'Rachel', 'Monica', 'Joey', 'Chandles', 'Phoebe']

def how_you_doing(*args):
    if args:
        for name in args:
            print(f'{name}, how you doing?')
    
      
print(how_you_doing())

def user_info(**kwargs):
    print(kwargs)
    for value in kwargs.values():
        print(value)

user_info(name = 'Ross', last_name = 'Geller', age = 35, has_children = True, cheat_Rachel = True)