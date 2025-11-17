from operations import sum, sub, mult
import random
import requests
import datetime 

def calculator():
    num1 = int(input('enter first number'))
    num2 = int(input('enter second number'))
    op = input('enter operation')
    if op == '+':
        result = sum(num1, num2)
    elif op == '-':
        result = sub(num1, num2)
    elif op == '*':
        result = mult(num1, num2)
    else:
        print('invalid operator')

    return result

print(calculator())