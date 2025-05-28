#Amy Zou_P5_2/21
#Random Image Generator

#Init
from PIL import Image
import requests
from io import BytesIO
import random
link = ["https://tinyurl.com/3nmpw3mu", #Gamerstopia. Zhongli: Talents, Ascension, Constellations. Angelo Lazaro. accessed via: https://tinyurl.com/yc65uw9k
        "https://tinyurl.com/276xdz57", #Gamerstopia. Venti: Talents, Ascension, Constellations. Angelo Lazaro. accessed via: https://tinyurl.com/bdhjaxpc
        "https://tinyurl.com/mss38cmx", #Gamerstopia. Raiden Shogun: Talents, Ascension, Constellations. Angelo Lazaro. accessed via: https://tinyurl.com/2ny6b8yx
        "https://tinyurl.com/ynnjvcc4", #Gamerstopia. Nahida: Talents, Ascension, Constellations. Angelo Lazaro. accessed via: https://tinyurl.com/2s3bj5zc
        "https://tinyurl.com/jsu3ntj7", #Hoyolab. furina it's here! Arka122. accessed via: https://www.hoyolab.com/article/22887003
        "https://tinyurl.com/zmddsrh5", #AsoWorld. Genshin Impact: Everything You Should Know about Mavuika. Jean L. accessed via: https://tinyurl.com/36x25kdj
         ]

#Function
#Define a function called open_image with a url parameter for the image address
def open_image(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()

def archon():
    print("Welcome to the Genshin Impact Archon Generator to help you determine which archon to pull for next")
    pull = input("Would you like to find an archon to pull for (y/n): ")
    while True:
        if pull == "y":
            x = random.randint(0,5)
            if x == 0:
                print("You should pull for Zhongli")
                print("He is a Geo polearm character. He has a very strong shield that is scaled off of his HP.")
                open_image(link[0])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break
            elif x == 1:
                print("You should pull for Venti")
                print("He is an Anemo bow character. He is great for crowd control.")
                open_image(link[1])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break
            elif x == 2:
                print("You should pull for Raiden Shogun")
                print("She is an Electro polearm character. She has great damage output with her burst and great electro application with her skill.")
                open_image(link[2])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break
            elif x == 3:
                print("You should pull for Nahida")
                print("She is a Dendro catalyst character. She is great for dendro application." )
                open_image(link[3])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break
            elif x == 4:
                print("You should pull for Furina")
                print("She is a Hydro sword character. She is great for hydro application.")
                open_image(link[4])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break
            elif x == 5:
                print("You should pull for Mavuika")
                print("She is a Pyro claymore character. She has great damage output with her burst and good pyro application with her skill.")
                open_image(link[5])
                again = input("Would you like to find another archon (y/n): ")
                if again == "n":
                    print("Best wishes in pulling the characters you want!")
                    break


#Main
archon()
