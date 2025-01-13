#Rock Paper Scissors

#Init
import random
wins = 0
loses = 0
ties = 0

#Function
#This function is the game that the player will be playing
#It introduces the player to the game and the player can play rock paper scissors with the computer
def game():
    print("""Welcome to the game
In this game, you will be playing rock paper scissors with the computer""")
    global wins
    global loses
    global ties
    while True:
        p_move = input("Please input your move, rock (r), paper (p), or scissors (s):")
        computer = random.randint(0,2)
        if computer == 0:
            c_move = "rock"
        elif computer == 1:
            c_move = "paper"
        elif computer == 2:
            c_move = "scissors"
        print("The computer has chosen "+ c_move + " as it's move")
        if p_move.casefold() == "r" and computer == 2:
            print("The player has won\n")
            wins = wins + 1
        elif p_move.casefold() == "r" and computer == 1:
            print("The player has lost\n")
            loses = loses + 1
        elif p_move.casefold() == "r" and computer == 0:
            print("The match has ended in a tie\n")
            ties = ties + 1
        elif p_move.casefold() == "p" and computer == 0:
            print("The player has won\n")
            wins = wins + 1
        elif p_move.casefold() == "p" and computer == 2:
            print("The player has lost\n")
            loses = loses + 1
        elif p_move.casefold() == "p" and computer == 1:
            print("The match has ended in a tie\n")
            ties = ties + 1
        elif p_move.casefold() == "s" and computer == 1:
            print("The player has won\n")
            wins = wins + 1
        elif p_move.casefold() == "s" and computer == 0:
            print("The player has lost\n")
            loses = loses + 1
        elif p_move.casefold() == "s" and computer == 2:
            print("The match has ended in a tie\n")
            ties = ties + 1
        else:
            print("An invalid move was made by the player")

        print("# of wins: " + str(wins))
        print("# of loses: " + str(loses))
        print("# of ties: " + str(ties))

        play = input("\nWould you like to play again? (y/n)")

        if play.casefold() == "n":
            print("These are your final stats: ")
            print("# of wins: " + str(wins))
            print("# of loses: " + str(loses))
            print("# of ties: " + str(ties))
            print("Thank you for playing")
            break

#Main
game()
