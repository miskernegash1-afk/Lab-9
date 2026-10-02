"""
Program Name: Match Coins Game
Author: Misker Negash
Purpose: This program runs a coin matching game between two players.
Starter Code: No starter code used.
Date: October 2, 2026
"""

from player import Player

# Runs the main game
def main():
 # Creates two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
 # Displays the starting number of coins
    print("--- Coin Match Game ---")
    print("Player 1 has", player1.get_wallet(), "coins.")
    print("Player 2 has", player2.get_wallet(), "coins.")

    play = input("\nDo you want to toss the coins? (y/n): ")