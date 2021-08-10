# This main.py file instantiates the chat bot and pulls communications from util.py

from util import get_beer_type, get_size

def chat_bot():
    print('Welcome to Cait\'s Brewery!')
    order_drink = 'y'
    drinks = []
    while order_drink == 'y':
        # Get the beer type and size
        beer_type = get_beer_type()
        size = get_size()

        # Repeat drink back to customer
        drink = '{} {}'.format(size, beer_type)
        print('Alright, I\'ve got a {} coming right up!'.format(drink))
        drinks.append(drink)
        # Option to order additional drinks
        while True:
            order_drink = input('Would you like to order another drink? (y/n)')
            if order_drink == 'y' or order_drink == 'n':
                break
    # Repeat order back to customer and close out
    print('Okay, so I have:')
    for order in drinks:
        print(order)
    name = input('Can I get your name please? \n> ')
    print('Thanks, {}! Your drinks will be out shortly.'.format(name))

# Run chat bot
chat_bot()