# Importing required module
import random
import string


def load_word():
    # Opens the word file and choose random word to guess
    with open('words_alpha.txt') as word_file:
        valid_words = list(set(word_file.read().split()))
        word = random.choice(valid_words)
    return word.upper()


def hangman():
    word = load_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    if len(word) < 8:
        lives = 6
    else:
        lives = 9

    # Getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ''.join(['a','b','cd']) --> 'a b cd'
        print('You have',lives, 'lives left and You have use these letters: ',''.join(used_letters))
        # Showing current word (i.e. w o - d)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))

        user_letter = input('Guess a letter: \n').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print("You have already guessed this letter")

        else:
            print("Please only input letters!!!!")

    if lives == 0:
        print(f"Sorry, You couln't guess in time. The correct word is \n {word}")
    else:
        print(f"Hurrayy!!! you guessed the word {word} correctly")

if __name__ == '__main__':
    hangman()