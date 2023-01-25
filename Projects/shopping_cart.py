# This project create an application that stores products within a list.
# We are able to add, remove, clear and show the products in the cart.



# Variable to store items
cart = []

# Create a function to add items to cart
def Additem(item):
    cart.append(item)
    print('{} has been added.'.format(item))
    
    
# Create a function to remove items from cart
def Removeitem(item):
    try:
        cart.remove(item)
        print('{} has been removed'.format(item))
    except:
        print('Sorry could not remove that item')
    
        
# Create a function to show items in the cart
def Showcart():
    if cart:
        print('Here is your cart')
        for item in cart:
            print('- {}'.format(item))
    else:
        print('Cart is empty.')
    
    
# Create function to clear items from cart
def Clearitem():
    cart.clear()
    print('Cart is empty.')
    


# Create the main function until user quits
def main():
    done = False
    while not done:
        ans = input('What do you want to do with you cart,\n quit/add/remove/show/clear? ').lower()
        if ans == 'quit':
            print('Thanks you.')
            Showcart()
            done = True
        elif ans == 'add':
            item = input('Enter the item you want to add').title()
            Additem(item)
        elif ans == 'remove':
            Showcart()
            item = input('What item would you want to remove?').title()
            Removeitem(item)
        elif ans == 'show':
            Showcart()
        elif ans == 'clear':
            Clearitem()
        else:
            print('That was not an option!')

# Call the main function
main()
