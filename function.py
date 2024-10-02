######## Function ########
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

######### Building A Simple Calculator #########
# print('Welcome to python pizza deliveries')
# total = 0
# def pizza_order():
#     global total
#     size = input('what size pizza do you want? S, M or L: ')
#     add_pepperoni = input('Do you want pepperoni? Y/N: ')
#     extra_cheese = input('Do you want extra cheese? Y/N: ')
    
#     if size == 'S':
#         total += 15
#     elif size == 'M':
#         total += 20
#     else:
#         total += 25
#     if add_pepperoni == 'Y':
#         if size == 'S':
#             total += 2
#         else: 
#             total += 3

#     if extra_cheese == 'Y':
#         total += 1
#     print(f'Your final tatol is £{total}')

# pizza_order() 

count = 0

def pizza_order():
    global count
    pizza = input('Choose your pizza: ')
    extra_topping = input('Do you want any extra toppings? (yes or no) ')
    if extra_topping.lower() == 'yes':
        extra = input('Choose an extra topping: ')
        print(f"Extra {extra} for your {pizza} pizza.")
    count += 1  # Increment count regardless of the toppings

    print(f'You have ordered {count} pizza(s)')

while True:
    pizza_order()
    another_order = input('Would you like to order another? (yes or no) ')
    if another_order.lower() != 'yes':
        break

print(f'Total pizzas ordered: {count}')
