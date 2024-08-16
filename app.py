import random
import time

def main_menu():
    print('Welcome to guess the number!')
    time.sleep(1)
    print('I am thinking of a number from 1 to 100.')
    time.sleep(1)
    print('Can you guess it?')
    time.sleep(3)
    gameplay_loop()

def gameplay_loop():
    guess_me = random.randint(1,100)
    player_guess = 0
    guesses = 0
    while player_guess != guess_me:
        player_guess = int(input('Enter your guess.'))
        if player_guess == guess_me:
            guesses += 1
            print(f'Congrats! You guessed the number in {guesses} tries.')
        if player_guess > guess_me:
            guesses += 1
            print('The number I am thinking of is smaller than that. Guess again!')
        if player_guess < guess_me:
            guesses += 1
            print('The number I am thinking of is larger than that. Guess again!')

main_menu()