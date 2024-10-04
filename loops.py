                           ######### Python Loops #########

        ####### FOR LOOPS #######
# for i in range(5):
#     print(i)

####### Activity 1: Count Up #######
# Task: Use a For Loop to print numbers from 1 to 20.​
# for i in range(20):
#     print(i+1)

####### Activity 2: Counting Down​ #######
# Task: Use a For Loop to print numbers from 20 down to 1.​
# for i in range(20, 0, -1):
#     print(i)

####### Activity 3: Every Second Character​ #######
# Task: Use a For Loop to print every second character from a given string, such as "Hello World!"​
# txt = 'Hello World!'
# for i in txt[1::2]:
#     print(i)

####### Activity 4: List Multiplier​ #######
# Task: Given a list of numbers, use a For Loop to print each number multiplied by 10.​
# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i * 10)


####### Activity 5: Adding Up​ #######
# Task: Use a For Loop to calculate the sum of numbers from 1 to 100 and print the result.
# num = 100
# sum = 0
# for i in range(1, num + 1):
#     sum += i
#     print(sum)

####### Activity 6: Finding Evens​ #######
# Task: Use a For Loop to print all even numbers from a list of integers.​
# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers :
#     if i % 2 == 0:
#         print(i)

####### Activity 7: Reverse Printing​ #######
# Task: Use a For Loop to print each item in a list in reverse order.​
# numbers = [1, 2, 3, 4, 5, 6]
# for i in reversed(numbers): 
#     print(i)

####### Activity 8: Skip Counting​ #######
# Task: Use a For Loop to print numbers from 1 to 50, but only multiples of 5.​
# for i in range (5, 51, 5):
#     print(i)

####### Activity 9: Concatenate Strings​ #######
# Task: Given a list of words, use a For Loop to concatenate them into a single string with spaces between words.​
# words = ['Hello', 'To', 'Everyone']
# result = ''
# for word in words:
#     result += word + ' '
#     print(result)


####### Activity 10: Factorial Finder​ #######
# Task: Use a For Loop to calculate the factorial of a given number and print the result.
# num = int(input('enter a number: '))
# factorial = 1
# for i in range(1, num, 1):
#     factorial *= i
# print(f'Factorial: {factorial}')

        ####### WHILE LOOPS #######
# num = 5
# counter = 0
# while variable == True:
#     counter += 1
#     print(f'this is an infinte loop {counter}')

####### Activity 1: Counting Up:​
#Write a program that asks the user for a starting number and counts up to that number using a while loop.​
# num = int(input('Enter any number; '))
# counter = 1
# while counter <= num:
#     print(counter)
#     counter += 1

####### Activity 2: Counting Down:​
#Create a program that prompts the user for a number and counts down to zero using a while loop.​
# num = int(input('Enter any number; '))
# counter = 0
# while num >= counter:
#     print(counter)
#     break
    
####### Activity 3: Sum of Numbers:​
#Write a program that calculates the sum of all numbers from 1 to a user-specified number using a while loop.​
# num2 = int(input("Enter a number: "))  
# x = 1  
# while x < 11:
#     print(x * num2)
#     x += 1

####### Activity 4: Guessing Game:​
#Implement a simple guessing game where the program generates a random number and the user has to guess it. Use a while loop to continue prompting the user until they guess correctly.​
# import random
# print("Welcome to the Guessing Game!")
# print("Try to guess the number I am thinking of between 1 and 10.")

# number = random.randint(1, 10)  # generate random number
# guess = -1  # initialize guess to an invalid value

# while guess != number:
#     guess_str = input("Enter your guess: ")
#     guess = int(guess_str)

#     if guess < number:
#         print("Too low, try again.")
#     elif guess > number:
#         print("Too high, try again.")

# print(f"Congratulations! You guessed the number {number} correctly!")

####### Activity 5: Password Guessing:​
#Create a program that prompts the user to enter a password. Keep prompting the user until they enter the correct password.​ 
# user_password = input('create any password? ')
# while(True):
#     passwordInput=input('PASSWORD: ')
#     if(passwordInput==user_password):
#         print("Login Successful")
#         break
#     else:
#         print("WRONG: please enter your password")