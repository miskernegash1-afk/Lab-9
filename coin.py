"""
Program Name: Match Coins Game - Coin Class
Author: Misker Negash
Purpose: This file creates a Coin class that can be tossed
and can keep track of whether it is Heads or Tails.
Starter Code: No starter code was used.
Date: October 2, 2026
"""

import random

# Creates the Coin class
class Coin:
    # Sets the starting side of the coin
    def __init__(self):
        self.__sideup = "Heads"
        # Randomly changes the coin to Heads or Tails
    def toss(self):
        number = random.randint(0, 1)

        if number == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"