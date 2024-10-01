#print("Hello World!")
#if 5 > 2:
#    print("Five is greater than two!")

# ifelse statment
# age = int(input('How old are you? '))
# if age <= 18:
#     print('you are too young to drink.')
# elif age >= 21:
#     print('you are eligible for a 21 and over discount.')

################ ACTIVITY 1 ####################
    # Task: Write a program that asks the user to input a number and then prints whether the number is positive or negative.
# num_input = int(input('Enter any number? '))
# if num_input > 0:
#     print(f'number {num_input} is positive number.')
# elif num_input < 0:
#     print(f'number {num_input} is negative number.')
# else:
#     print(f'number {num_input} is neither a positive or negative number.')

################ ACTIVITY 2 ####################
    # Task: Ask the user to input a number. Print whether the number is even or odd.
# even_or_odd_input = int(input('Enter any number? '))
# if (even_or_odd_input % 2) == 0:
#     print(f'number {even_or_odd_input} is even number.')
# else:
#     print(f'number {even_or_odd_input} is odd number.')

# ################ ACTIVITY 3 ####################
    # Task: Write a program that asks the user for two numbers and prints which one is larger, or if they are equal.
# value_one, value_two = input('Enter two values? ').split()
# max_num = max(value_one, value_two)
# print(f'number {max_num} is larger, between {value_one} and {value_two}')

# ################ ACTIVITY 4 ####################
    # Task: Write a program that checks if a year (input from the user) is a leap year or not.
# leap_year = int(input('enter a year? '))
# if (leap_year % 4 == 0 and leap_year % 100 != 0 ) or ( leap_year % 400 == 0 ):
#     print('hurray its a leap year')
# else:
#     print('it not a leap year')

# ################ ACTIVITY 5 ####################
# Task: Write a program that converts a numeric grade (0-100) into a letter grade (A, B, C, D, F).
# grade = int(input('Enter your grade? '))
# if grade <= 20:
#     print('you got an F')
# elif grade <= 40:
#     print('you got an D')
# elif grade <= 60:
#     print('you got an C')
# elif grade <= 90:
#     print('you got an B')
# elif grade <= 100:
#     print('you got an A')
# else:
#     print('please enter your grade again?')

# ################ ACTIVITY 6  ####################
# Task: Ask for the user's age and categorize them into 'Child', 'Teenager', 'Adult', or 'Senior'.
# age_group = int(input('enter your age? '))
# if age_group <= 2:
#     print('you are a baby.')
# elif age_group <= 12:
#     print('you are a child.')
# elif age_group <= 19:
#     print('you are a teenager.')
# elif age_group <= 39:
#     print('you are a adult.')
# elif age_group <= 59:
#     print('you are a middle age.')
# else:
#     print('you are a senior')


# ################ ACTIVITY 7 ####################
# Task: Write a program that suggests an activity based on the temperature input by the user. For example, above 20 degrees could suggest going outside.
# temperature = float(input("Enter the temperature: "))
# if temperature > 20:
#     print("Its a great day to go outside!")
# else:
#     print("You might want to stay inside.")

# ################ ACTIVITY 8 ####################
#Task: Check if an input number is divisible by both 5 and 10 or just by 5, just by 10, or neither.
# number = int(input("Enter a number: "))
# if number % 5 == 0 and number % 10 == 0:
#     print("The number is divisible by both 5 and 10.")
# elif number % 5 == 0:
#     print("The number is divisible by 5.")
# elif number % 10 == 0:
#     print("The number is divisible by 10.")
# else:
#     print("The number is not divisible by 5 or 10.")

# ################ ACTIVITY 9 ####################
# Task: Create a simple calculator that asks the user for two numbers and an operation to perform on them (+, -, *, /).
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Enter the operation (+, -, *, /): ")
# if operation == "+":
#     print(f"The result is: {num1 + num2}")
# elif operation == "-":
#     print(f"The result is: {num1 - num2}")
# elif operation == "*":
#     print(f"The result is: {num1 * num2}")
# elif operation == "/":
#     if num2 != 0:
#         print(f"The result is: {num1 / num2}")
#     else:
#         print("Error: Division by zero is not allowed.")
# else:
#     print("Invalid operation")

# ################ ACTIVITY 10 ####################
# Task: Write a program that checks if a number is within a range specified by two other numbers (inclusive).
# number = int(input("Enter a number: "))
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# if start <= number <= end:
#     print(f"{number} is within the range {start}-{end}.")
# else:
#     print(f"{number} is not within the range {start}-{end}.")
 