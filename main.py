# Python Text RPG
# Names: Matt DeRespinis, 

import cmd
import textwrap
import sys
import os
import time
import random
import shutil

terminal_width = shutil.get_terminal_size().columns
width = 50

##### PLAYER CLASS #####
class player:
    def __init__(self):
        self.name = ""
myPlayer = player()

##### TITLE SCREEN #####
def titleScreen():
    print("+================================================+")
    print(str.center("Welcome to Unearthed Echoes", width))
    print("+================================================+")
    print("1. New Game")
    print("2. Help")
    print("3. Quit")

titleScreen()