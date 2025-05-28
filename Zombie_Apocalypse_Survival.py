#Zombie Apocalypse Survival

#Init
health = 50
supplies = 0
allies = 0
enemies = 0
name = "name"

#Function
def intro():
    global name
    print("Welcome to the Zombie Apocalypse Survival")
    print("You will be asked to select choices which will affect your final outcome, so choose wisely")
    food = input("Please input a food you hate:")
    print("Some mad scientist decided to make a new virus which ended up turning anyone who ate " + food + " to be a zombie")
    print("Luckily you don't like " + food + " so you haven't been turned into a zombie")
    name = input("What would you like to be called?")
    print(name + ", your goal is to survive and save as many people as possible to ensure that humanity doesn't go extinct")
    play = input("Are you up for the challenge? (yes/no)")
    if play.casefold() == "yes":
        start_game()
    elif play.casefold() == "no":
        print("It's ok, someone else will save the world")


def start_game():
    while True:
        global allies
        global health
        global supplies
        global name
        global enemies
        ans = "nothing"
        if ans == "no":
            break
        else:
            print("You meet a person named Ty, he seems like an outgoing person and even offered you some food because he thought you were hungry")
            choice_1 = input("Would you like to befriend this person (yes/no): ")
            if choice_1.casefold() == "yes":
                allies = allies + 1
                supplies = supplies + 10
                health = health + 20
                print("You have made a nice choice and your allies have increased to " + str(allies))
                print("Because you befriended Ty, you got some supplies which increased your health to " + str(health))
                explore = input("Where do you and Ty want to go explore (hospital/supermarket/town): ")
                if explore == "hospital":
                    explore_hospital()
                    break
                elif explore == "supermarket":
                    explore_supermarket()
                    break
                elif explore == "town":
                    explore_town()
                    break

            elif choice_1.casefold() == "no":
                print("You denied the food thinking that there was something in the food that could kill you")
                print("Because you denied the food he offered, he became wary of you")
                print("Luckily for you, you found a supermarket to get the food you needed and it also has all the other resources you would need")
                choice_2 = input("Do you want to set up your base at this supermarket (yes/no):")
                if choice_2 == "yes":
                    print("The wary Ty was very unhappy that you were hoarding resources and has told everyone he knows not to trust or get close to you")
                    enemies = enemies + 1
                    print("Though Ty became an enemy of you, you were able to save the world by ensuring humanity wouldn't go extinct")
                    print("Congratulations for saving the world")
                    ans = input("Would you like to play again (yes/no): ")
                    if ans == "yes":
                        intro()
                    elif ans == "no":
                        print("Thank you for reading this story and playing along")
                        break
                elif choice_2 == "no":
                    health = health/5
                    print("Your health has dropped to " + str(health))
                    choice_3 = input("Would you like to try to befriend Ty to get some food (yes/no): ")
                    if choice_3 == "yes":
                        print("Ty was wary that you are suddenly being nice to him")
                        print("He didn't give you any food so you died")
                        break
                    elif choice_3 == "no":
                        print("You have died")
                        ans = input("Would you like to play again (yes/no): ")
                        if ans == "no":
                            print("Thank you for reading this story and playing along")
                            break


def explore_hospital():
    global allies
    global health
    global supplies
    global name
    global enemies
    health = health - 2
    print(name + " and Ty have made it to the hospital\nYou didn't encounter anything serious along the way")
    print("Your current health is " + str(health))
    print("Since you are at the hospital you two decide to look around for resources and people")
    separate = input("Would you like to split up from Ty (yes/no): ")
    if separate == "yes":
        print("You encountered a lot of zombies which you could not fight off")
        print("You have died")
        ans = input("Would you like to play again (yes/no): ")
        if ans == "yes":
            intro()
        elif ans == "no":
            print("Thank you for reading this story and playing along")
    elif separate == "no":
        print("You have found 10 people 5 of which could be infected")
        choice = input("Would you like to save the 5 which are not infected (yes/no): ")
        if choice == "no":
            print("You died because everyone got infected")
            ans = input("Would you like to play again (yes/no): ")
            if ans == "yes":
                intro()
            elif ans == "no":
                print("Thank you for reading this story and playing along")

        elif choice == "yes":
            print("Saving those people allowed you to form a team, so you all worked together to kill the remaining zombies in the hospital")
            print("You were able to set up a base which allowed for humanity to not go extint")
            print("Congratulations for saving the world")
            ans = input("Would you like to play again (yes/no): ")
            if ans == "yes":
                intro()
            elif ans == "no":
                print("Thank you for reading this story and playing along")



def explore_town():
    global allies
    global health
    global supplies
    global name
    global enemies
    health = health - 2
    print(name + " and Ty have made it to the town\nYou didn't encounter anything serious along the way")
    print("Your current health is " + str(health))
    print("Upon arriving at the town, lots of zombies come running towards you two")
    print("Both of you died from the zombie attack")
    ans = input("Would you like to play again (yes/no): ")
    if ans == "yes":
        intro()
    elif ans == "no":
        print("Thank you for reading this story and playing along")



def explore_supermarket():
    global allies
    global health
    global supplies
    global name
    global enemies
    health = health - 2
    print(name + " and Ty have made it to the supermarket\nYou didn't encounter anything serious along the way")
    print("Your current health is " + str(health))
    print("Since you are at the supermarket you two decide to look around for any resources")
    separate = input("Would you like to split up from Ty (yes/no): ")
    if separate == "yes":
        print("You encountered a lot of zombies which you could not fight off")
        print("You have died")
        ans = input("Would you like to play again (yes/no): ")
        if ans == "yes":
            intro()
        elif ans == "no":
            print("Thank you for reading this story and playing along")

    elif separate == "no":
        print("You and Ty explore the supermarket and find lots of supplies")
        print("You are able to set up a base and save many others, preventing humanity from going extinct")
        print("Congratulations, you svaed the world!")
        ans = input("Would you like to play again (yes/no): ")
        if ans == "yes":
            intro()
        elif ans == "no":
            print("Thank you for reading this story and playing along")


#Main
intro()
