# multi-line strings
# methods
# lists
# append() and reverse() list
# lower(), upper(), split(), startswith(), endswith() string methods
# in and not in
# range() and list()
# del statementss
# for loops
# elif statements

import random
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
      |
      |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
 ======== ''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
 ======== ''']
words = "ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra".upper()
words = words.split()


def getRandomWord(wordList):
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    print("Missed letters: ", end=" ")
    if len(missedLetters)==0:
        print("NONE", end=" ")
    else:
        for letter in missedLetters:
            print(letter, end=" ")
    print()
    blanks = "_" * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
        print(blanks[i], end=" ")
    print()
def getGuess(alreadyGuessed):
    while True:
        print("Guess a letter", end =": ")
        guess = input()
        guess = guess.upper()
        if len(guess)!=1:
            print("Please enter a single letter")
        elif guess in alreadyGuessed:
            print("You already guessed this letter")
        elif guess not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print("please enter a LETTER")
        else:            
            return guess
    
def playAgain():
    print("Would you like to play again? (yes or no)")
    return input().lower().startswith("y")

#main
print("WELCOME TO HANGMAN")
missedLetters = ""
correctLetters=""
secretWord = getRandomWord(words)
gameIsDone= False


while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    guess = getGuess(missedLetters+correctLetters)
    if guess in secretWord:
        correctLetters = correctLetters + guess
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print("Yes! The secret word is " + secretWord + "! You win!")
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess
        if len(missedLetters)== len(HANGMANPICS)-1:
            displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
            print("You have run out of guesses!")
            print("You correctly guessed " + str(len(correctLetters)) +" letters")
            print("The secret word was " + secretWord)
            gameIsDone= True
    if gameIsDone:
        if playAgain():
            missedLetters = ""
            correctLetters =""
            gameIsDone= False
            secretWord = getRandomWord(words)
        else:
            print("Thanks for playing")
            break
        
