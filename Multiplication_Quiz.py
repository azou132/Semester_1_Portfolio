#Multiplication Quiz

#Init
import random
import time

#Function

#This function is a simple game of muliplication
#it allows the player to choose what mode they want to play, how many questions they want, and if they want to time themselves
def simple_game():
    print("Welcome to the Multiplication Quiz!")
    print("There are three modes you can choose, easy, hard, and endless")
    print("You can time yourself (if you want) in easy and hard mode")
    choice = input("What difficulty do you want the questions to be (easy/hard/endless):")
    start_time = 0
    end_time = 0
    total_time = 0
    if choice.casefold() == "easy":
        while True:
            question_max = int(input("How many questions would you like to have?"))
            question = 1
            correct = 0
            incorrect = 0
            timer = input("Would you like to time yourself (y/n): ")
            if timer.casefold() == "y":
                start_time = time.time()
            for i in range(question_max):
                num1 = random.randint(0,10)
                num2 = random.randint(0,10)
                correct_ans = num1 * num2
                print("Question " + str(question) + " of " + str(question_max) + ": ")
                ans = int(input("Please solve " + str(num1) + " * " + str(num2) + ": "))
                if ans == correct_ans:
                    correct = correct + 1
                    question = question + 1
                else:
                    incorrect = incorrect + 1
                    question = question + 1
            end_time = time.time()
            total_time = end_time - start_time
            print("You got " + str(correct) + " out of " + str(question_max) + " questions correct!")
            if timer.casefold() == "y":
                print("You answered the questions in " + str(round(total_time,2)) + " seconds!")
            choice = input("Would you like to continue playing (y/n):")
            if choice.casefold() == "n":
                print("Thank you for playing!")
                break
            elif choice.casefold() == "y":
                choice = input("Would you like to play a harder level (y/n):")
                if choice.casefold() == "y":
                    difficult_game()
                    break
    elif choice.casefold() == "hard":
        difficult_game()
    elif choice.casefold() == "endless":
        endless_game()

#This function is the difficult version of the game
#It asks the player how many questions they want and if they want to time themselves
def difficult_game():
    start_time = 0
    end_time = 0
    total_time = 0
    while True:
        question_max = int(input("How many questions would you like to have?"))
        timer = input("Would you like to time yourself (y/n): ")
        if timer.casefold() == "y":
            start_time = time.time()
        question = 1
        correct = 0
        incorrect = 0
        for i in range(question_max):
            num1 = random.randint(0,20)
            num2 = random.randint(0,20)
            correct_ans = num1 * num2
            print("Question " + str(question) + " of " + str(question_max) + ": ")
            ans = int(input("Please solve " + str(num1) + " * " + str(num2) + ": "))
            if ans == correct_ans:
                correct = correct + 1
                question = question + 1
            else:
                incorrect = incorrect + 1
                question = question + 1
        end_time = time.time()
        total_time = end_time - start_time
        if timer.casefold() == "y":
            print("You answered the questions in " + str(round(total_time,2)) + " seconds!")
        print("You got " + str(correct) + " out of " + str(question_max) + " questions correct!")
        choice = input("Would you like to continue playing (y/n):")
        if choice.casefold() == "n":
            print("Thank you for playing!")
            break
        elif choice.casefold() == "y":
            endless = input("Would you like to play the endless mode (y/n): ")
            if endless == "y":
                endless_game()
            elif endless == "n":
                break

#This function is the endless mode of the game, continuous questions ranging from any multiplication between 0 and 12
#lets the player know how many questions they got correct at the end
def endless_game():
    question = 1
    correct = 0
    incorrect = 0
    while True:
        num1 = random.randint(0,12)
        num2 = random.randint(0,12)
        correct_ans = num1 * num2
        print("Question " + str(question) + " of " + str(question) + ": ")
        ans = int(input("Please solve " + str(num1) + " * " + str(num2) + ": "))
        if ans == correct_ans:
            correct = correct + 1
            question = question + 1
        else:
            incorrect = incorrect + 1
            question = question + 1
        choice = input("Continue questions (y/n):")
        if choice.casefold() == "n":
            print("You got " + str(correct) + " out of " + str(question - 1) + " questions correct!")
            print("Thank you for playing!")
            break

#Main
simple_game()
