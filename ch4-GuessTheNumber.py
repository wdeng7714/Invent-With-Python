# Guess the number game
import random
number = random.randint(1, 20)
guessesTaken= 0
print('Hello! What is your name?')
playerName=input()
print('Welcome ' + playerName + ', I am tinking of a number between 1 and 20')
while guessesTaken<6:
    print('Take a guess: ')
    guess = input()
    guess = int(guess)
    guessesTaken=guessesTaken+1
    if guess == number:
        break
    if guess > number:
        print('Your guess is too high')
    if guess < number:
        print('Your guess is too low')

if guess ==number:
    print('You win! You guessed the number in '+ str(guessesTaken) + ' guesses!')
if guess != number:
    print('You lose! The secret number is ' + number)
