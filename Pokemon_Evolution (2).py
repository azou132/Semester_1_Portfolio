#Pokemon Evolution

#Init
import random
pokemon_level = 0
pokemon_name = 'squirtle'
win = 0
loss = 0

#Function
#This function draws out squirtle who is the starter pokemon
def squirtle():
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⠤⠤⠤⠤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠢⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⢀⣀⡐⢄⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠁⠀⠀⠀⠀⠀⡜⠁⠀⣿⡌⠀⠀⠀⠀⠀⠀⠀⠀⠈⢆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⠀⠀⣸⣷⣤⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠊⣼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢤⡀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⡜⣼⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠉⠲⣄⣀⣼⡇⠀⠀⠀⠀⠀⠀⠻⠿⣿⣟⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠉⠁⠀⡏⠑⠌⠓⢬⣧⠀⠀⠀⠀⠘⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠿⡀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⠀⠀⠀⠇⠀⠀⠀⠀⠙⣆⠀⠀⠀⠀⠀⠈⠉⠓⠒⠲⠤⢤⣀⠀⠂⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀
⠀⠀⠀⠀⢀⣠⠤⠖⠒⠒⠒⠦⢤⡀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠲⠤⠤⠒⠋⢉⠟⠀⠀⠀⠀
⠀⠀⢀⡴⠋⠁⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⢠⡞⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠋⠀⠀⠀⠀⠀
⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀⢠⡟⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡏⠈⠑⠢⢤⣀⣀⠀⠀⠀⠀⢀⣀⡤⠖⠯⣀⠀⠀⠀⠀⠀⠀
⢀⡟⠀⠀⠀⠀⠠⠴⠤⣀⠀⠀⠀⠀⠀⢸⣠⡟⠀⠀⠀⠀⢹⣄⠀⠀⠀⠀⠀⠀⢀⣼⡁⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⢻⠀⠀⠀⠀⠀⠉⠢⣄⣀⡀⠀
⢸⡇⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⢈⣿⡇⠀⠀⠀⠀⢸⠉⢢⣀⡀⢀⣀⣴⠟⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⢇⡀
⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢸⡇⣷⠀⠀⠀⢀⡞⠀⢰⠏⠉⠉⠁⢸⡀⠀⠀⠀⠈⠓⠶⠤⣤⣄⣀⣠⡤⠴⡇⠀⠀⠀⠀⠀⠀⠀⠀⡔⠁
⠀⠹⣆⠀⠀⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⢸⠁⠸⡆⠀⣠⠞⠀⢀⡞⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⢰⣧⣀⣀⡀⠀⢀⣀⣠⠴⠃⠀
⠀⠀⠹⡓⠦⠤⠤⠖⠋⠀⠀⠀⠀⠀⠀⢸⠀⠀⠹⡴⠁⠀⢠⠞⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡞⠀⠀⠀⣸⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀
⠀⠀⠀⠘⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⢁⡠⠴⢧⡀⠀⠀⠀⠀⣀⠔⠳⣄⠀⠀⠀⠀⠀⠀⡼⠁⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇⣠⡿⠋⠀⠀⠀⠙⢦⣀⡠⠞⠁⠀⠀⠈⠙⠶⣤⣀⡀⣰⠃⠀⠀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⠀⠀⠀⠀⠀⠀⣸⠏⠀⠀⠀⠀⠀⠀⠈⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣹⠋⠉⠉⣹⠏⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠲⢤⣄⣀⣠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⢀⣤⠞⠁⠀⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⠶⠤⠤⠤⠤⠤⢤⣞⡥⠖⠋⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠒⠀⠀⠒⠒⠺⢯⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀⠀⠀⠀⠀⠀⢄⣈⠆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⢄⡀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠀⠀⢀⣠⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢇⣀⡤⠖⢄⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⠒⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠈⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

#This function draws out wartortle which is the first evolution of squirtle
def wartortle():
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠹⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⡶⠖⢶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⣆⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⣋⠁⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⢹⡄⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⣡⡾⠉⠀⢀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠃⠀⠀⠘⣇⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⢡⡾⠋⠀⠀⢀⡾⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⣿⠀⣿⠀⢀⣠⣤⡴⠶⠶⠒⠒⠶⠶⢤⣄⣀⠀⢀⣼⠋⣴⠏⠀⠀⠀⠀⠚⠁⣸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⢸⢀⣿⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⡾⠃⣸⠇⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣬⣷⡀⠀⢀⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃⠀⡟⠀⠀⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠉⠃⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⠇⠀⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⡀⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⠀⠼⠀⠀⠀⠀⠀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠘⣷⡀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠶⠛⠋⠉⠉⠙⠛⢶⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠙⣧⠀⠈⠛⠷⠦⢤⣶⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣾⡉⣿⣄⢀⡀⠀⠀⠀⠀⣀⠀⣠⣾⣯⣽⣷⠀⢹⡆⠀⠀⠀⠀⢸⡏⣷⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⢀⡾⠛⠛⠷⠀⠀⠀⠸⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡟⡇⣿⣿⡟⠇⠀⠀⠀⠀⠿⠞⠋⢸⣿⣿⣿⠀⢸⡇⠀⠀⠀⠀⣾⠁⢸⡷⣦⣀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠸⣇⠀⠀⠀⠀⠀⠀⢠⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⠁⢹⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡛⣿⢀⣼⠇⠀⠀⠀⣼⠷⠖⠛⠛⠛⠛⠷⠶⠶⣤⣼⣇⣀⠀⠀⠀⠀⠀⠻⣦⣀⣀⣀⣠⡴⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣀⣤⡤⠶⠞⠻⣷⣤⣀⠙⠃⣀⠀⢀⡀⠀⠀⠀⠀⠀⠈⠛⠃⠈⢁⣠⣼⣧⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⣛⣷⣦⡀⠀⠀⢹⠹⡏⠉⠉⢷⡀⠀⠀⠀
⠀⠀⢀⣤⠶⣾⠛⠉⠁⠀⠀⠀⠀⠈⠛⠿⣿⣷⣯⣄⣈⣡⣤⣤⣤⣤⡤⠴⠶⠶⢿⣿⣿⡾⠛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⡀⠘⣿⣦⡀⢸⠀⠁⠀⠀⠈⣷⠀⠀⠀
⠀⣴⢾⡃⣰⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠻⠿⣭⣭⣤⣀⣀⣀⣠⣤⣤⣶⣾⠟⠉⠀⠀⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠛⢿⣿⣤⣿⡽⠇⣿⢀⣠⣤⣤⣄⣹⡄⠀⠀
⠘⢿⣼⣿⣯⣴⠶⢲⡆⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠉⠻⢿⣿⣟⣻⣿⠿⠋⠁⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣤⡴⠿⠋⠀⠀⢰⣿⡟⠉⠀⠀⠈⠙⢷⣄⠀
⠀⠀⠈⠻⢿⣶⣤⣿⠁⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠉⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⢀⣀⣀⣤⣤⠶⠟⢿⡅⠀⠀⠀⠀⢠⡿⣿⠀⠀⣴⢶⣄⠀⠀⠹⣆
⠀⠀⠀⠀⠀⠈⠉⠉⠛⠛⠓⠶⠶⠶⠶⠶⣾⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⣿⠉⢸⠀⠀⠀⢸⡇⠀⠀⠀⣠⡟⠁⠹⣦⡀⠀⣠⡿⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣯⠀⢸⣇⠀⠀⢸⡇⠀⠀⠚⠋⠀⠀⠀⠈⠙⠛⠋⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣷⣤⣀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡶⠟⢻⡀⠀⢿⡄⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡌⠉⠛⠶⠶⣤⣤⣄⣸⣇⣀⣀⣀⣠⣤⣤⠴⠶⠞⠛⠉⠀⠀⠀⠈⣷⣄⣀⢻⣆⣾⡇⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⢀⣾⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡄⠀⠀⠀⠀⠀⠀⠉⢿⡉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠉⠉⠙⠷⣿⣿⠇⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢠⡾⠁⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠋⠈⢻⣆⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⣀⣴⠾⠋⠀⠀⠀⠀⠀⢀⣴⠟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠁⠀⠀⠀⠙⢷⣄⠀⠀⠀⠀⢀⣼⣧⣤⣀⡀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣯⣉⣤⠄⠀⠀⠀⠀⣠⡴⠟⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⣠⡴⠟⠁⠀⠀⠉⠙⠛⠷⠶⢦⣴⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⢀⣀⣤⠶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⢘⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠈⠙⠛⠓⠶⠶⠶⠖⠛⠛⠛⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠷⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠓⠻⣇⠀⣀⣠⣤⡀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠟⠋⠁⠈⠛⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣃⣀⣤⣄⡀⠀⠀⣠⣴⠦⣤⣄⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠋⠉⠀⠈⠙⠳⠾⠟⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

#This function draws out blastiose who is the final version of squirtle
def blastiose():
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠶⠶⠶⠚⠋⠉⠉⠉⠛⠃⠀⠉⣿⡆⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣏⣿⣿⣶⠀⠀⠀⣸⣿⠉⣳⣶⠾⠐⠛⠛⠉⠉⠙⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣼⣿⠋⠀⠀⠀⠛⠛⠉⠁⠀⠀⠀⠀⠘⠻⠶⠖⠚⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠀⣀⣴⠀⠀⠀⠀⠀⢀⣠⡴⠞⠋⠉⣻⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣇⣀⣀⣀⣸⠋⠙⠛⠶⠶⠖⠚⠋⠁⠀⠀⠀⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⠤⢤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⠴⠾⠛⠛⠛⠳⠿⢭⣍⣛⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⣠⡾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠙⢧⡀⠀⢀⣀⡀⠀⣠⡴⠞⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⠽⢿⡶⢯⣿⣦⡀⠀⢀⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢻⣄⠀⠀⠀⠀⢈⣿⠞⠋⢩⣿⣿⠿⠶⠒⠒⠲⠶⢤⣄⣀⠤⠶⠞⠛⠉⠁⠀⠀⣸⠃⣤⡙⢯⡻⣿⣉⣡⡤⠴⠶⢢⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠹⣦⠀⢀⡴⠋⠁⣠⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⢀⡟⢠⣿⠿⣬⣻⣾⠋⠀⠀⠀⠀⠀⠀⢸⣿⣇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣳⠟⠁⣠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⣸⠃⠀⠈⠉⢹⡀⠀⠀⠀⠀⠀⠀⠀⢿⣿⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⠋⢀⣾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣿⢀⡿⠰⣆⠀⢀⣼⢷⡀⠀⠀⠀⠀⣀⣀⣨⡽⠃⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠃⣠⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⢸⡇⢸⣇⣠⣽⡶⠟⠀⢈⡿⠓⠚⠛⠉⡟⠻⣦⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡾⣿⣷⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣄⡀⠀⠀⠀⠀⠘⣧⠸⣿⡟⠀⠀⠀⠀⣼⠁⠀⠀⠀⢀⡇⠀⠈⠻⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⠁⢿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠉⠙⠻⢶⣤⡀⠀⢹⡆⢹⣇⠀⠀⠀⠀⡿⠀⠀⠀⠀⣼⠁⠀⠀⠀⢹⡿⣦⡀⠀⠀
⠀⠀⠀⠀⣿⣧⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠋⠀⠀⠀⠀⠀⠈⠙⢷⣤⣻⡄⢿⡄⠀⠀⠀⡇⠀⠀⢀⣼⠋⠀⠀⠀⠀⢀⡇⠈⢷⠀⠀
⠀⠀⠀⠀⠉⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣼⢿⡄⠀⠀⣇⣤⡶⠋⠁⠀⠀⠀⠀⠀⣼⠃⠀⢸⣷⡄
⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠋⠀⢷⠀⢀⡿⣤⣀⡀⠀⠀⠀⢀⣠⡾⠃⢀⣤⢿⡷⣿
⠀⠀⠀⠀⣸⢿⡀⢀⣀⣀⣀⣀⣀⣀⡀⢀⣠⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⢸⣄⣼⠇⠀⡿⠉⠉⠛⠛⠛⠷⠲⣿⡏⠛⠾⠇⠀
⠀⠀⠀⠀⣿⣼⠟⠉⠉⠉⠉⠉⠉⠉⠉⠛⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⣼⠟⣷⡆⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡾⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⢠⡇⠀⠘⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡟⠀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⠁⠀⠀⠀⠀⢀⣠⣾⡛⠳⢶⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣼⠁⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠹⣦⠀⠙⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡏⠀⠀⣸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠘⣧⠀⠈⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠀⣿⠻⣆⣠⡤⠶⠶⠶⢦⣄⡀⠀⠀⠀⢹⡆⠀⣀⣤⠶⠋⠁⠀⠀⠀⠀⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⡇⠀⠀⢸⡆⠉⠁⠀⠀⠀⠀⠀⠈⠙⠷⣤⡤⠾⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣷⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣧⠀⠀⠀⢷⣤⠶⠛⠉⠉⠙⠓⠶⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢹⡶⠶⢶⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣤⣤⡴⠶⠚⠛⠉⠉⠉⠉⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⣸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡟⠀⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠁⠀⠀⠀⢀⣀⣀⣤⡴⠶⠛⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢛⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠛⠛⠛⠛⠉⠉⠉⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠛⠋⠙⠻⢶⡄⠀⠀⠀⠀⢀⣼⠋⠙⢿⣟⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⠶⠤⠤⠤⠤⠤⠶⠶⠚⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣤⣤⣤⡤⠶⠾⠗⠛⠛⠛⠉⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

#This function determines the level the pokemon will evolve at and which version it will evolve into
def evolve():
    global pokemon_name
    if pokemon_level >= 10 and pokemon_level <= 19:
        pokemon_name = 'wartortle'
    elif pokemon_level >= 20:
        pokemon_name = 'blastiose'

#This function displays the pokemon's information
def display():
    print("Your pokemon's name is: " + pokemon_name)
    print("Your pokemon's level is: " + str(pokemon_level))
    print("Win:" + str(win))
    print("Loss:" + str(loss))
    if pokemon_name == "squirtle":
        print("This is your pokemon: ")
        squirtle()
    elif pokemon_name == "wartortle":
        print("This is your pokemon: ")
        wartortle()
    elif pokemon_name == "blastiose":
        print("This is your pokemon: ")
        blastiose()

#This function introduces the game to the player
def intro():
    print('''Welcome to the Pokemon Evolution Game
In this game you can train your pokemon to make them the strongest they can be''')
    print('Your current pokemon is squirtle, they are at level 0')

#This function is the game that the player will play
#It has a menu and training features to allow the player to advance further
def game():
    while True:
        global win
        global loss
        global pokemon_level
        print("Choose your activity:")
        if pokemon_level >= 20:
            print('1. Train\n2. Gym Battle\n3. Display Pokemon information\n4. Exit\n5. Final Battle')
            mode = int(input('1-5:'))
        else:
            print('1. Train\n2. Gym Battle\n3. Display Pokemon information\n4. Exit')
            mode = int(input('1-4:'))
        if mode == 1:
            pokemon_level = pokemon_level + 1
            print("Congratulations, your pokemon's level has increased to level " + str(pokemon_level))
            if pokemon_level == 10:
                print('Congratulations, your pokemon has evolved into a wartortle \nDisplay pokemon information to see your newly evolved pokemon!')
            elif pokemon_level == 20:
                print('Congratulations, your pokemon has evolved into the final evolution!\n Display pokemon information to see your newly evolved pokemon!')
        elif mode == 2:
            if pokemon_level >= 5 and pokemon_level <= 8:
                outcome = random.randint(1,2)
            else:
                outcome = 1
            if outcome == 1:
                pokemon_level = pokemon_level + 2
                win = win + 1
                print("Congratulations you won the gym battle, your pokemon's level has increased to level " + str(pokemon_level))
                if pokemon_level == 10 or pokemon_level == 11:
                    print('Congratulations, your pokemon has evolved into a wartortle\nDisplay pokemon information to see your newly evolved pokemon!')
                elif pokemon_level == 20 or pokemon_level == 21:
                    print('Congratulations, your pokemon has evolved into the final evolution!\nDisplay pokemon information to see your newly evolved pokemon!')
            else:
                loss = loss + 1
                print("You lost the gym battle, train your pokemon more and try again")
        elif mode == 3:
            evolve()
            display()
        elif mode == 5:
            print('Wow, you reached the final hidden level')
            ans = input("This boss challenge is harder than anything you have seen, are you ready? (y/n):")
            if ans == "y":
                if pokemon_level >= 20 and pokemon_level <=22:
                    outcome = random.randint(1,100)
                elif pokemon_level >= 23 and pokemon_level <=24:
                    outcome = random.randint(1,20)
                elif pokemon_level >= 25 and pokemon_level <= 27:
                    outcome = random.randint(1,2)
                elif pokemon_level >= 28:
                    outcome = 1
                if outcome == 1:
                    win = win + 1
                    print('Yay, you won the final battle!\nThank you for playing!')
                    ans = input("Would you like to look at your final stats before exiting? (y/n)")
                    if ans == "y":
                        display()
                        break
                    elif ans == "n":
                        break
                else:
                    loss = loss + 1
                    print("Train your pokemon more and try again!")
            elif ans == 'n':
                print("It's okay, come back once you have increased your pokemon's level")
        elif mode == 4:
            print("Thank you for playing")
            break

#Main
intro()
game()

