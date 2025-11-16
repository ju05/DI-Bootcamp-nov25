# create a class called BankAccount, with 3 attributes:
#- account houlder = name + last name of a person
#- account number = random number
#- balance which starts with 50.00 (float)
import datetime

class BankAccount:

    def __init__(self, houlder, acc_number, balance = 50.00):
        self.houlder = houlder
        self.acc_number = acc_number
        self.balance = balance
        self.transactions = []

    def view_balance(self):
        self.transactions.append(f'{datetime.datetime.now()} --- view_balance')
        report = f'''account holder: {self.houlder}
                account number: {self.acc_number}
                balance: {self.balance}'''
        print(report)

    def deposit(self, amount):
        self.transactions.append(f'{datetime.datetime.now()} --- deposit {amount}')
        if amount <= 0:
            print('invalid amount')
        else:
            self.balance += amount

        self.view_balance()
        return self.balance

    def withdraw(self, amount):
        self.transactions.append(f'{datetime.datetime.now()} --- withdraw {amount}')
        if amount <= 0:
            print('invalid amount')
        elif self.balance < amount:
            print('You dont have enouph money')
        else:
            self.balance -= amount

        self.view_balance()
        return self.balance
    
    def view_transactions(self):
        for transaction in self.transactions:
            print(transaction)
    

#creating the first account on BankAccount
acc1 = BankAccount('Juliana Schmidt', '1234567')
acc1.view_balance() #50
acc1.deposit(500)
acc1.withdraw(700)
acc1.view_transactions()
# acc1.view_balance()

#create a new attribute called transactions. it is a list.
