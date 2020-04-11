
# function to display menu items
def display_menu():
    menu_items = '''
    1. Add (+)
    2. Sub (-)
    3. Mul (*)
    4. Div (/)
    '''
    print('-' * 20)
    print(menu_items)
    print('-' * 20)


# get value from user and convert them to number
def get_value():
    n1 = float(input('Number One: '))
    n2 = float(input('Number Two: '))
    return n1, n2

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

# x and y are parameters
def div(x, y):
##    try:
##        return x / y
##    except ZeroDivisionError:
##        return 'You cannot divide by zero'

    if y == 0:
        return 'You cannot divide by zero'
    else:
        return x / y


while True:
    display_menu()
    user_response = input('> ')

    if user_response == '1':
        n1, n2 = get_value()
        print('Result is', add(n1, n2))
    elif user_response == '2':
        n1, n2 = get_value()
        print('Result is', sub(n1, n2))
    elif user_response == '3':
        n1, n2 = get_value()
        print('Result is', mul(n1, n2))
    elif user_response == '4':
        n1, n2 = get_value()
        print('Result is', div(n1, n2))  # n1 and n2 are arguments
    else:
        print('Error')
        break
