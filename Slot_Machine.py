#Slot Machine

#Init
import random
import time
symbols = ['7', '☾', '☆ ', '❀ ', '❄ ', '✾ ']
credits = 0
cost = 10
ans = " "
add = " "
print(symbols)

#Function
def slot_machine():
    global credits
    global ans
    global add
    print("Welcome to the slot machine where you can win BIG")
    print("Each spin costs 10 credits, you can win 50 credits from hitting a jackpot, and 10 credits if you get a match")
    print("A jackpot consists of getting three 7 while a match is just 3 of the same symbol")
    print("You can also set a bet in which you can choose how much your spin will cost and you can get however much you bet back, \nso betting 10 would give you 20 back with a profit of 10")
    print("However, you can only bet the amount you have")
    print("Slot Machine Symbols: " + str(symbols))
    credits = int(input("How many credits would you like to start off with: "))
    print("Current Credits: " + str(credits))
    start = input("Would you like to spin, bet, or quit (s/b/q):")
    while True:
        if start == "s":
            slot_1 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
            slot_2 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
            slot_3 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
            if credits <= 9:
                add = input("You don't have enough credits, would you like to add more? (y/n)")
                if add == "y":
                    more = int(input("How many credits would you like to add: "))
                    credits = credits + more
                elif add == "n":
                    print("You can not play anymore")
                    break
            credits = credits - cost
            print("Spinning ... ")
            time.sleep(1)
            print("Current Slots: " + str(slot_1) + str(slot_2) + str(slot_3))
            if slot_1 == "7" and slot_1 == slot_2 and slot_2 == slot_3:
                print("You hit the jackpot!")
                print("You have won 50 credits")
                credits = credits + 5*cost
                ans = input("Would you like to continue (s/q): ")
                if ans == "q":
                    print("Final Credits: " + str(credits))
                    print("Thank you for playing!")
                    break
            elif slot_1 == slot_2 and slot_2 == slot_3:
                print("You made a match!")
                print("You have won 25 credits")
                credits = credits + cost
                ans = input("Would you like to continue (s/q): ")
                if ans == "q":
                    print("Final Credits: " + str(credits))
                    print("Thank you for playing!")
                    break
            elif slot_1 == slot_2 or slot_2 == slot_3 or slot_3 == slot_1:
                print("You got two of a kind!")
                print("You have won 5 credits")
                credits = credits + 1/2*cost
                ans = input("Would you like to continue (s/q): ")
                if ans == "q":
                    print("Final Credits: " + str(credits))
                    print("Thank you for playing!")
                    break
            else:
                print("You didn't win, but you surely will next time!")
                ans = input("Would you like to continue (s/q): ")
                if ans == "q":
                    print("Final Credits: " + str(credits))
                    print("Thank you for playing!")
                    break

        elif start == "b":
            bet()
            if ans == "q":
                break
            if add == "n":
                break

        elif start == "q":
            print("Final Credits: " + str(credits))
            print("Thank you for playing!")
            break


def bet():
    global credits
    global ans
    global add
    while True:
        slot_1 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
        slot_2 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
        slot_3 = random.choices(symbols, weights = [1, 10, 10, 10, 10, 10])
        betAmount = int(input("How much would you like to bet, keep in mind that you can only bet the amount of credits you have: "))
        winType = input("What would you like to bet for, 3 of a kind, 2 of a kind, or jackpot (3/2/j): ")
        if credits < betAmount:
            add = input("You don't have enough credits, would you like to add more? (y/n)")
            if add == "y":
                more = int(input("How many credits would you like to add: "))
                credits = credits + more
            elif add == "n":
                print("You can not play anymore")
                break
        credits = credits - betAmount
        print("Spinning ... ")
        time.sleep(1)
        print("Current Slots: " + str(slot_1) + str(slot_2) + str(slot_3))

        if slot_1 == "7" and slot_1 == slot_2 and slot_2 == slot_3 and winType == "j":
            print("You hit the jackpot and you bet for the jackpot!")
            print("You have won " + str(2*betAmount) + " credits")
            credits = credits + 2*betAmount
            ans = input("Would you like to continue (b/q): ")
            if ans == "q":
                print("Final Credits: " + str(credits))
                print("Thank you for playing!")
                break
        elif slot_1 == slot_2 and slot_2 == slot_3 and winType == "3":
            print("You made a match which you bet for!")
            print("You have won " + str(2*betAmount) + " credits")
            credits = credits + 2*betAmount
            ans = input("Would you like to continue (b/q): ")
            if ans == "q":
                print("Final Credits: " + str(credits))
                print("Thank you for playing!")
                break
        elif slot_1 == slot_2 or slot_2 == slot_3 or slot_3 == slot_1 and winType == "2":
            print("You got two of a kind which you bet for!")
            print("You have won " + str(2*betAmount) + " credits")
            credits = credits + 2*betAmount
            ans = input("Would you like to continue (b/q): ")
            if ans == "q":
                print("Final Credits: " + str(credits))
                print("Thank you for playing!")
                break
        else:
            print("You didn't win, but you surely will next time!")
            ans = input("Would you like to continue (b/q): ")
            if ans == "q":
                print("Final Credits: " + str(credits))
                print("Thank you for playing!")
                break

#Main
slot_machine()
