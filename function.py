                                    ######## Functions ########

# occation_input = input('what is the occation? ')
# name_input = input('what is your name? ')
# def create_greet_card(occasion, name):
#     if occasion.upper() == 'birthday':
#         print(f'happy birthday, {name}')
#     elif occasion == 'morning':
#         print(f'good morning,{name}')
#     else: 
#         print(f'good day, {name}')
# create_greet_card(occation_input, name_input)

######### Building A Simple Calculator #########
# def simple_calculator():
#     print('simple Calculator - add, subtract, multiply and divide')
#     num1 = int(input('Any Number: '))
#     operation = input('Add, Subtract, Multiple and divide: ')
#     num2 = int(input('Any Number: '))

#     if operation == 'add' :
#         result = num1 + num2
#         print(f'{num1} + {num2} = {result}')
#     elif operation  == 'subtract' :
#         result =num1 - num2
#         print(f'{num1} - {num2} = {result}')
#     elif operation  == 'multiply':
#         result = num1 * num2
#         print(f'{num1} * {num2} = {result}')
#     elif operation  == 'divide':
#         result = num1 / num2
#         print(f'{num1} / {num2} = {result}')
#     else:
#         print('Did not understand')

# simple_calculator()

######### Building A Pizza Order #########
print('Welcome to python pizza deliveries')
total = 0
def pizza_order():
    global total
    size = input('what size pizza do you want? s, m or l: ')
    add_pepperoni = input('Do you want pepperoni? y/n: ')
    extra_cheese = input('Do you want extra cheese? y/n: ')
    
    if size == 's':
        total += 15
    elif size == 'm':
        total += 20
    else:
        total += 25
    if add_pepperoni == 'y':
        if size == 's':
            total += 2
        else: 
            total += 3

    if extra_cheese == 'y':
        total += 1
    print(f'Your final tatol is £{total}')

pizza_order() 
