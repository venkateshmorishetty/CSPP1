'''Hangman game'''
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = len(secretWord)
    i = 0
    total = 0
    while i < count:
        if secretWord[i] in lettersGuessed:
            total = total + 1
        else:
            break
        i = i + 1
    if total == count:
        return True
    return False
def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    count = len(secretWord)
    result = ''
    i = 0
    while i < count:
        if secretWord[i] in lettersGuessed:
            result += secretWord[i]
        else:
            result += '_'
        i = i + 1
    return result
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    result = ''
    a = string.ascii_lowercase
    print(a)
    result = [i for i in a if i not in lettersGuessed]
    return ''.join(result)
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("welcome to Hangman")
    lettersGuessed = []
    print("your guessing string contain", len(secretWord), "letters")
    print("-----------------------------------")
    check = False
    maxnoofguess = len(secretWord)+5
    print(getGuessedWord(secretWord, lettersGuessed))
    while maxnoofguess != 0:
        print("you have", maxnoofguess, "left")
        print("avilable letters:", getAvailableLetters(lettersGuessed))
        guess = input("enter your guess")
        maxnoofguess -= 1
        lettersGuessed.append(guess)
        check = isWordGuessed(secretWord, lettersGuessed)
        if check:
            break
        print(getGuessedWord(secretWord, lettersGuessed))
    if check:
        print("congrats")
    else:
        print("better luck next time")
    print(secretWord)
# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
 