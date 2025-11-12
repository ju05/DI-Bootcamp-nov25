#copy dict and wallet from the platform

# items_purchase = {"Water": "$1", "Bread": "$3", "TV": "$1,000", "Fertilizer": "$20"}
# wallet = "$300"

# items_purchase = {"Apple": "$4", "Honey": "$3", "Fan": "$14", "Bananas": "$4", "Pan": "$100", "Spoon": "$2"}
# wallet = "$100"

items_purchase = {"Phone": "$999", "Speakers": "$300", "Laptop": "$5,000", "PC": "$1200"}
wallet = "$1"

#clean the data (prices and wallet)
cleaned_wallet = int(wallet.replace('$', ''))

#create an empty list called basket
basket = []

for item, price in items_purchase.items():
    cleaned_price = int(price.replace('$', '').replace(',', ''))
    if cleaned_price <= cleaned_wallet:
        basket.append(item)
        cleaned_wallet -= cleaned_price
    else:
        continue

if basket:
    print(sorted(basket))
else:
    print('nothing')

#check if the item is affordable (check the price):
# - if it is, add to the basket and take the price from the wallet
# - if not, skip it
# if we can't buy anything: print 'nothing'
# if we can buy something: print the basket in alphabetical order

