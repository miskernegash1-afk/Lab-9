"""
Program Name: Match Coins Game
Author: Misker Negash
Purpose: This file creates the Player class for the Match Coins game.
Starter Code: No starter code used.
Date: October 2, 2026
"""

from coin import Coin

# Creates the Player class
class Player:
 # Sets the player's name, starting wallet, and coin
    def __init__(self, name):
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()
            # Tosses the player's coin
    def toss_coin(self):
        self.__coin.toss()

    # Returns the result of the coin toss
    def get_coin_side(self):
        return self.__coin.get_sideup()