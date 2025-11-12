import random

def compare_num(user_num):
    computer_num = random.randint(1, 100)
    if user_num == computer_num:
        print('Success!')
    else:
        print(f'{computer_num}, Fail')

compare_num(55)

def get_random_temp():
    temp = random.randint(-10, 40)
    return temp

def main():
    temp = get_random_temp()
    if temp < 0:
        print('Brrr, that\'s freezing! Wear some extra layers today.')