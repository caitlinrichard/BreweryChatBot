# Contains messaging prompts for the chat bot

# Default message if someone does not choose from menu items
def print_message():
    print('I\'m sorry, I did not understand your order. Please enter the corresponding letter for your response.')

# Get customer's type of beer they want
def get_beer_type():
    res = input('What type of beer would you like? \n[a] IPA \n[b] Stout \n[c] Sour \n> ')

    if res == 'a':
        return order_IPA()
    elif res == 'b':
        return order_stout()
    elif res == 'c':
        return order_sour()
    else:
        print_message()
        return get_beer_type()

# Get the pour size
def get_size():
    res = input('What size pour would you like? \n[a] 12 oz \n[b] 16 oz \n> ')

    if res == 'a':
        return '12 oz'
    elif res == 'b':
        return '16 oz'
    else:
        print_message()
        return get_size()

# Additional options if user selects IPA
def order_IPA():
    res = input('And what kind of IPA? \n[a] hazy \n[b] fruit \n[c] milkshake \n> ')

    if res == 'a':
        return 'hazy IPA'
    elif res == 'b':
        return 'fruit IPA'
    elif res == 'c':
        return 'milkshake IPA'
    else:
        print_message()
        return order_IPA()

# Additional options if user selects stout
def order_stout():
    res = input('And what kind of stout? \n[a] milk \n[b] oatmeal \n[c] coffee \n> ')

    if res == 'a':
        return 'milk stout'
    elif res == 'b':
        return 'oatmeal stout'
    elif res == 'c':
        return 'coffee stout'
    else:
        print_message()
        return order_stout()

# Additional options if user selects sour
def order_sour():
    res = input('And what kind of sour? \n[a] cherry \n[b] pineapple \n[c] blueberry \n> ')

    if res == 'a':
        return 'cherry sour'
    elif res == 'b':
        return 'pineapple sour'
    elif res == 'c':
        return 'blueberry sour'
    else:
        print_message()
        return order_sour()