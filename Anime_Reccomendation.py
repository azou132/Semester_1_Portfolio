#Anime Reccomendation

#Init
print ('Welcome to Anime Recommendations')
print ('Answer questions to find out what anime you should watch')

#Function
#This function determines which anime is reccomended based on what the person chooses
def watch_anime():
    ans = input('romance (r) or adventure (a)')

    if ans == 'r':
        ans = input('sad (s) or drama (d)')
        if ans == 's':
            ans = input('bullies (b) or memories (m)')
            if ans == 'b':
                print('You should watch A Silent Voice')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
            elif ans == 'm':
                print('You should watch Your Name')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
        elif ans == 'd':
            ans = input('rain (r) or war (w)')
            if ans == 'r':
                print('You should watch Weathering With You')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
            else:
                print("You should watch Howl's Moving Castle")
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')

    elif ans == 'a':
        ans = input('animals (a) or spirits (s)')
        if ans == 'a':
            ans = input('cat (c) or fish (f)')
            if ans == 'c':
                print('You should watch My Neighbor Totoro')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
            elif ans == 'f':
                print('You should watch Ponyo')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
        elif ans == 's':
            ans = input('death (d) or mythical (m)')
            if ans == 'd':
                print('You should watch Spirited Away')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')
            else:
                print('You should watch Suzume')
                choice = input('Would you like to find another anime to watch (yes or no)')
                if choice == 'yes':
                    watch_anime()
                elif choice == 'no':
                    print('Thank you for playing, hope you enjoy the anime!')

#Main
watch_anime()
