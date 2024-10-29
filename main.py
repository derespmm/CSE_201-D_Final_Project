# Python Text RPG
# Names: Matt DeRespinis, Teddy Simpson, Dylan Kendall

import cmd
import textwrap
import sys
import os
import time
import timeit
import random
import shutil
import item as i

terminal_width = shutil.get_terminal_size().columns
width = 50


class Player:
    """A class for the player character."""
    def __init__(self, name):
        self.name = name
        self.inventory = i.Inventory()


myPlayer = Player("Jon")
otherPlayer = Player("Matthew")


def title_screen():
    """A title screen wow!"""
    print("+================================================+")
    print(str.center("Welcome to Unearthed Echoes", width))
    print("+================================================+")
    print("1. New Game")
    print("2. Help")
    print("3. Quit")


title_screen()
