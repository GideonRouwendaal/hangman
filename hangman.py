import random

""" hangman
    Created on 1 June 2020
    @author: Gideon Rouwendaal
    @python_version: Python 3.9
    """

attempts = 0
MAX_ATTEMPTS = 6
guessed_letters = []
unknown_word = []
DICTIONARY_NL = "nederlands3.txt"
DICTIONARY_EN = "sowpods.txt"
ASCII_HANGMAN_0 = """
  +---+
  |   |
      |
      |
      |
      |
=========
    """
ASCII_HANGMAN_1 = """
  +---+
  |   |
  O   |
      |
      |
      |
=========
    """
ASCII_HANGMAN_2 = """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
    """
ASCII_HANGMAN_3 = """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
    """
ASCII_HANGMAN_4 = """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
    """
ASCII_HANGMAN_5 = """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
    """
ASCII_HANGMAN_6 = """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
    """


def check_ASCII():
    if attempts == 0:
        return ASCII_HANGMAN_0
    elif attempts == 1:
        return ASCII_HANGMAN_1
    elif attempts == 2:
        return ASCII_HANGMAN_2
    elif attempts == 3:
        return ASCII_HANGMAN_3
    elif attempts == 4:
        return ASCII_HANGMAN_4
    elif attempts == 5:
        return ASCII_HANGMAN_5


def getindexpositions(word, letter_guessed):
    # Get index/indices of the letter which is guessed in the word
    word = list(word)
    indexPosList = []
    for i in range(len(word)):
        if word[i] == letter_guessed:
            indexPosList.append(i)
    return indexPosList


def create_unknown_word():
    for i in range(word_length):
        unknown_word.append("_")


def print_unknown_word():
    result = ""
    for i in range(word_length):
        result += unknown_word[i]
    return result


def check_if_letter_guessed(letter_guessed):
    if letter_guessed in guessed_letters:
        letter_guessed = str(
            input("You have already guessed this letter. Type the letter you think the word contains: "))
        return check_if_letter_guessed(letter_guessed)
    else:
        return letter_guessed


def check_letter(letter_guessed):
    # Check how many occurrences there are in the word and return the amount
    return word.count(letter_guessed)


def letters_guessed():
    # Return a string which contains the letters which are guessed
    result = ""
    for i in range(len(guessed_letters)):
        result += guessed_letters[i] + " "
    return result


def check_word_guessed():
    if "_" in unknown_word:
        return False
    else:
        return True


def check_length(letter):
    if len(letter) > 1:
        letter = str(
            input("You have entered several letters. Type a single letter you think the word contains: "))
        return check_length(letter)
    else:
        return letter

def replace_by_letter(indices, guessed_letter):
    for i in range(len(indices)):
        unknown_word[indices[i]] = guessed_letter


def check_properties(letter):
    if len(letter) > 1:
        letter = str(
            input("You have entered several letters. Type a single letter you think the word contains: "))
        return check_properties(letter)
    if letter in guessed_letters:
        letter = str(
            input("You have already guessed this letter. Type the letter you think the word contains: "))
        return check_properties(letter)
    return letter


def choose_dicitonary():
    choice = int(input("Type a 1 if you want an English word and a 2 if you want a Dutch word: "))
    if choice == 1:
        return DICTIONARY_EN
    elif choice == 2:
        return DICTIONARY_NL
    else:
        return choose_dicitonary()


choice = choose_dicitonary()
dictionary = open(choice).readlines()
dictionary_length = len(dictionary)

word = dictionary[random.randint(0, dictionary_length)].lower()
# Do minus 1, to delete the linebreak
word_length = len(word) - 1
create_unknown_word()

print(word)

while attempts < MAX_ATTEMPTS and (check_word_guessed() == False):
    print(check_ASCII())
    print("The word is: %s" % print_unknown_word(), "\n")
    print("The letters you have already guessed are: %s" % letters_guessed(), "\n")
    letter_guessed = str(input("Type the letter you think the word contains: "))

    # check if the letter guessed has already been guessed and add the letter to the guessed_letters list
    letter_guessed = check_properties(letter_guessed)
    guessed_letters.append(letter_guessed)

    # check the amount of occurrences of the guessed letter in the word
    occurrences = check_letter(letter_guessed)

    if occurrences == 0:
        attempts += 1
    else:
        indices_replace_by_letter = getindexpositions(word, letter_guessed)
        replace_by_letter(indices_replace_by_letter, letter_guessed)

if attempts == 6:
    print(ASCII_HANGMAN_6)
    print("You did not guess the word! Noob!!")
    print("The word is: %s" % word)
else:
    print("Good job!! You guessed the word %s right!" % word)