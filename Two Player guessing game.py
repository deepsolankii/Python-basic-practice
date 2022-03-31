# Two Player guessing game

import random

# Define the play function


def play(a, b, original_number):
    print("Please enter your guess:\n")
    guess = 0
    while True:
        try:
            guess_num = int(input())
        except ValueError:
            print("Please enter only integers")
        guess = guess + 1
        if guess_num < a or guess_num > b:
            print("You are guessing out of range")
        elif guess_num > original_number:
            print("Wrong Guess !!!!   Please guess lower number")
        elif guess_num < original_number:
            print("Wrong Guess !!! Please guess a higher number")
        elif guess_num == original_number:
            print("Congratulations!! You have guessed the number correctly ")
            print(f"Number of guesses you took : {guess} \n")
            return guess


if __name__ == '__main__':

    # Take range from user
    a = int(input("Please Enter the lower bound of your range:\n"))
    b = int(input("Please Enter the upper bound of your range:\n"))
    original_number1 = random.randint(a, b)
    print("player 1: It's your turn")
    guess_1 = play(a, b, original_number1)
    print("player 2: It's your turn")
    original_number2 = random.randint(a, b)
    guess_2 = play(a, b, original_number2)

    # Decide the winner
    if guess_1 < guess_2:
        print("Player 1 is the winner!!!!!")
    elif guess_1 > guess_2:
        print("Player 2 is the winner!!!!!")
    else:
        print("It's a tie !!!!!!")
