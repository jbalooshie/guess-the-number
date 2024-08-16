import random
import time

def greeting():
    print('Welcome to guess the number!')
    time.sleep(1)
    print('I am thinking of a number from 1 to 100.')
    time.sleep(1)
    print('Can you guess it?')
    time.sleep(3)

def gameplay_loop():
    guess_me = random.randint(1,100)
    player_guess = 0
    guesses = 0
    while True:
        try:
            player_guess = int(input('Enter your guess.'))
        except ValueError:
            print('You did not guess a number. Try again.')
            continue

        if player_guess > 100 or player_guess < 0:
            print('That is not a valid guess! The number is from 1 to 100.')
        elif player_guess > guess_me:
            guesses += 1
            print('The number I am thinking of is smaller than that. Guess again!')
        elif player_guess < guess_me:
            guesses += 1
            print('The number I am thinking of is larger than that. Guess again!')
        else:
            guesses += 1
            print(f'Congrats! You guessed the number in {guesses} tries.')
            break
        

def play_again():
    time.sleep(3)
    choice = ''
    while True:
        choice = input('Would you like to play again? Y/N')
        if choice == 'Y':
            print("Ok! I'm thinking of a new number.")
            time.sleep(1)
            return True
        elif choice == 'N':
            time.sleep(1)
            return False
        else:
            print('Invalid selection.')

def main_menu():
    greeting()
    while True:
        gameplay_loop()
        if not play_again():
            print('Thanks for playing!')
            break

if __name__ == '__main__':
    main_menu()