# create addition function
def add(x, y):
    return x + y

#create subtraction function
def subtract(x, y):
    return x - y

#create multiplication function
def multiply(x, y):
    return x * y

#create division function
def divide(x, y):
    if y == 0:
        return 'Érror! Division by zero is not allowed !!!!'
    else:
        return x / y

#create calclator functions to choose from
def calculator():
    print('Select operation:')
    print('1. add')
    print('2. subtract')
    print('3. multpily')
    print('4. divide')

while True:
    #Take input from the user
    choice = input('enter choice (1/2/3/4): ')

#check if the input is one of the four options
    if choice in ['1', '2', '3', '4']:
        num1 = float(input('Enter first number: '))
        num2 = float(input('Enter second number: '))

#calling the functions to work
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        if choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        if choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        if choice == '4':
            print(f"{num1} / {num2} = {divide(num1, num2)}")
    #option to exit the loop
    nextCalculation = input('Do you want to do another calculation? (yes/no): ')
    if nextCalculation != 'yes':
        break

print('Exiting calculator. Goodbye!')
# call the calculator function
calculator()








