# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    for item, price in menu_dict.items():
        print(f'{item} - {price}₪')


def add_item(menu_dict):
    """Add a new drink to the menu."""
    item = input('Enter the item name: ')
    if item in menu_dict:
        print('Item already exists!')
    else:
        price = float(input('Enter the price with decimal: '))
        menu_dict[item] = price
        print('Item was added to the menu')

def update_price(menu_dict):
    """Change the price of an existing drink."""
    item = input('Which item you would like to update?')
    if item in menu_dict:
        price = float(input('Enter the new price: '))
        menu_dict[item] = price
        print(f'{item} price was updated')
    else:
        print('item is not on the menu')


def delete_item(menu_dict):
    """Remove a drink from the menu."""
    item = input('Which item you would like to delete?')
    if item in menu_dict:
        del menu_dict[item]
        print('item was deleted')
    else:
        print('item is not on the menu')


def show_options():
    """Print the available actions."""
    options = '''What would you like to do?
                1. Show menu
                2. Add item
                3. Update price
                4. Delete item
                5. Exit'''
    print(options)


def run_coffee_shop(menu):
    """Main loop of the program."""

    while True:
        show_options()
        choice = input('What would you like to do?')

        if choice == '1':
            show_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            update_price(menu)
        elif choice == '4':
            delete_item(menu)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print("Invalid choice, try again.")

# Start the program
run_coffee_shop(menu)