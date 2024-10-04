######### Hangman Game ##########
# importing the time module
import time
import random

# welcoming the user
name = input('Player 1, What is your name? ')
print(f'Hello {name}. Time to play hangman! ')

# wait for 1 second
time.sleep(1)
print('Start guessing...')
time.sleep(0.5)

# here we set the secret. you can select any word
word = ['success', 'reedom', 'courage', 'charity', 'respect', 'comfort', 'honesty', 'helpful', 'triumph', 'quality']
random_word = random.choice(word)
guesses = ''
turns = 10

while turns > 0:
    failed = 0
    for char in random_word:
        if char in guesses:
            print(char, end=' ')
        else: 
            print('_', end=' ')
            failed += 1
    if failed == 0:
        print(' You Won')
        break
    guess = input(' guess another word: ')
    guesses += guess
    if guess not in random_word:
        turns -= 1
        print('Wrong')
        print(f'You have, {turns} more gueses')
        if turns == 0:
            print('You Lose')




print(random_word)