class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
        
    def __int__(self):
        return int(self.amount)
    
    def __repr__(self):
        if self.amount == 1:
            return f'{self.amount} {self.currency}'
        else:
            return f'{self.amount} {self.currency}s'
        
    def __add__(self, other):
        if type(other) != int and self.currency == other.currency:
            return self.amount + other.amount
        elif type(other) == int:
            return self.amount + other
        else:
            raise TypeError(f'Cannot add between Currency type {self.currency} and {other.currency}')
        
    def __iadd__(self, other):
        if type(other) != int:
            result = self.amount + int(other.amount)
            self.amount = result
            return self
        else:
            result = self.amount + int(other)
            self.amount = result
            return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

#the comment is the expected output
print(c1)
# '5 dollars'

print(int(c1))
# # 5

print(repr(c1))
# # '5 dollars'

print(c1 + 5)
# # 10

print(c1 + c2)
# # 15

print(c1) 
# 5 dollars

c1 += 5
print(c1)
# 10 dollars

c1 += c2
print(c1)
# 20 dollars

print(c1 + c3)
# # TypeError: Cannot add between Currency type <dollar> and <shekel>