import re
import colorama
from colorama import Fore,Back

def split_word(word):
    return list(word)

def compare_letters(guessed_letter, correct_letter):
    if guessed_letter == correct_letter:
        return True
    else:
        return False

def check_letter(guessed_letter,num, correct_word):
    letters = split_word(correct_word.upper())
    for i in range(len(letters)):
        if compare_letters(guessed_letter, letters[i]) == True and i == num:
            return True, True
            break
        elif compare_letters(guessed_letter, letters[i]) == True and i != num:
            return True, False
            break
        else:
            continue
    return False, False
        

guesses = 0
word = "WORDS"
print("welcome to the wordle game\nyou will be asked to guess a 5 letter word in 6 guesses")

for i in range (6):
    valid = False
    while valid == False:
        guess = input("guess word\n")
        if len(guess) > 5:
            print ("Error! Only 5 characters allowed!")
        else:
            valid = True       

    guess = split_word(guess.upper())
    correct_letter = False
    correct_place = False

    for i in range(5):
        correct_letter,correct_place = check_letter(guess[i],i,word)
        if correct_letter == True and correct_place == True:
            print(Fore.BLACK + Back.GREEN + f"{guess[i]}", end="")
        elif correct_letter == True and correct_place == False:
            print(Fore.BLACK + Back.YELLOW + f"{guess[i]}", end="")
        else:
            print(Fore.WHITE + Back.BLACK + f"{guess[i]}", end="")
    print()
    