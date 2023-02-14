import json
from difflib import get_close_matches
import random
from colored import stylize,fore, back, style,fg, bg, attr


# create a function to get the the meaning
def Get_meaning(word):
    for i in data[word]:
        return i

# Define a function to get the meaning of a word.


def Unknown_format(word):
    unknownform = '_'*len(word)

    # If the word contains an apostrophe, add it to the unknown format string.
    if "'" in word:
        indexex = [index for index, char in enumerate(word) if char == "'"]
        for index in indexex:
            unknownform = unknownform[:index]+"'"+unknownform[index+1:]

    # If the word contains a space or hyphen, add it to the unknown format string.
    if ' ' in word or '-' in word:
        indexex = [index for index, char in enumerate(
            word) if char == ' ' or char == '-']
        for index in indexex:
            unknownform = unknownform[:index]+' '+unknownform[index+1:]
        return unknownform
    else:
        return unknownform


# load the data of json file
# (here file name is dict.json)
data = json.load(open("dict.json"))
# Choose a random word from the `data` dictionary.
word = random.choice(list(data.keys()))
word.lower()
# Set the number of allowed guesses to 7.
mistake_limit = 7
# Get the unknown format of the word.
unknown_form = Unknown_format(word)
# Create an empty list to store the guessed letters.
guessed_letters = []
print(f'{fg("104")}try to guess the word you have {mistake_limit} mistake limit at forth youll be given a description')
print("this word contains", len(unknown_form), "letters"+attr("reset"))

# Start an infinite loop to play the game.
while True:
    print(fg("30") + style.BOLD+unknown_form+attr("reset"))
    guess = str(input('guess a letter  ')).lower()

    # Check if the letter has already been guessed.
    if guess in guessed_letters or guess in unknown_form:
        print('you already said that you idiot')

    elif guess in word:
        # Identify the indexes of the guessed letter in the word.
        indexes = [index for index, char in enumerate(word)
                   if char == guess]
        print('yes theres some of that')
        # Replace the corresponding letters in the unknown format with the guessed letter.
        for i in indexes:
            unknown_form = unknown_form[:i]+guess+unknown_form[i+1:]

            # Check if the player has won.
        if word == unknown_form:
            print('you win')
            break

    # If the letter is not in the word.
    else:
        mistake_limit = mistake_limit-1
        guessed_letters.append(guess)
        print('there is no '+guess+' in this word')
        print(mistake_limit, '\n', guessed_letters)
        if mistake_limit == 3:
            print(Get_meaning(word))
        if mistake_limit == 0:
            print(
                "you lost you idiot if you can't solve this piece"
                " of shit your going to be nothing in your life",
                fg("9") + style.BOLD+"\n by the way the word was: ", word+attr("reset"))
            break
print(fg("30")+Get_meaning(word)+attr('reset'))
