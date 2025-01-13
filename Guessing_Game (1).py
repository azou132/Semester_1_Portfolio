#Guessing Game

#Init
import random

#Function

#This function introduces the game and asks the player what difficulty they want the game to be
def intro():
    print('Welcome to the Guessing Game!')
    print('This game involves guessing a number')
    print('You can play the game by inputting an integer')
    print('If the number you guessed was the same as the secret number, you win!')
    ans = input('Would you like to play? (yes or no)')
    if ans == 'yes':
        ans = input('Choose your difficulty of the game (easy/medium/hard)')
        if ans == 'easy':
            print('This difficulty has you guess between 0 and 10')
            game(0,10)
        elif ans == 'medium':
            print('This difficulty has you guess between 0 and 50')
            game(0,50)
        elif ans == 'hard':
            print('This difficulty has you guess between 0 and 100')
            game(0,100)
    elif ans == 'no':
        print('Thank you for your time :)')

#This function allows for the player to choose the difficulty and changes the numbers they can guess between accordingly
def play():
    ans = input('Choose your difficulty of the game (easy/medium/hard)')
    if ans == 'easy':
        print('This difficulty has you guess between 0 and 10')
        game(0,10)
    elif ans == 'medium':
        print('This difficulty has you guess between 0 and 50')
        game(0,50)
    elif ans == 'hard':
        print('This difficulty has you guess between 0 and 100')
        game(0,100)

#This is the game and two integers need to be put in for it to work
#These two integers determine the values the player has to guess between
def game(x,y):
    guess = int(input('Enter guess') )
    secret = random.randint(x,y)
    if guess == secret:
        print('You guessed correctly!')
        ans = input('Would you like to play again? (yes or no)')
        if ans == 'yes':
            play()
        elif ans == 'no':
            print('Thank you for playing!')
    else:
        print('You guessed incorrectly :(')
        if secret <= guess:
            guess = int(input('Your guess was too high, try again:'))
            if guess == secret:
                print('You guessed correctly!')
                ans = input('Would you like to play again? (yes or no)')
                if ans == 'yes':
                    play()
                elif ans == 'no':
                    print('Thank you for playing!')
            else:
                print('You guessed incorrectly :(')
                print('So close, the answer was ' + str(secret) + ', good try though')
                ans = input('Would you like to play again? (yes or no)')
                if ans == 'yes':
                    play()
                elif ans == 'no':
                    print('Thank you for playing!')

        elif secret > guess:
            guess = int(input('Your guess was too low, try again: '))
            if guess == secret:
                print('You guessed correctly!')
                ans = input('Would you like to play again? (yes or no)')
                if ans == 'yes':
                    play()
                elif ans == 'no':
                    print('Thank you for playing!')
            else:
                print('You guessed incorrectly :(')
                print('So close, the answer was ' + str(secret) + ', good try though')
                ans = input('Would you like to play again? (yes or no)')
                if ans == 'yes':
                    play()
                elif ans == 'no':
                    print('Thank you for playing!')
#Main
intro()

