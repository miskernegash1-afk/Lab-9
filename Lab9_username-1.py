"""
Program Name: Match Coins Game
Author: Misker Negash
Purpose: This program runs a coin matching game between two players.
Starter Code: No starter code used.
Date: October 2, 2026
"""

from Player import Player

# Runs the main game
def main():
 # Creates two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")
 # Displays the starting number of coins
    print("--- Coin Match Game ---")
    print("Player 1 has", player1.get_wallet(), "coins.")
    print("Player 2 has", player2.get_wallet(), "coins.")
# Asks the user if they want to play
    play = input("\nDo you want to toss the coins? (y/n): ")
        

    # Keeps the game running while the user enters y or Y
    while play == "y" or play == "Y":

        print("\nTossing...")
                # Tosses both players' coins
        player1.toss_coin()
        player2.toss_coin()

        # Gets the result of each coin
        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        # Displays the toss results
        print("Player 1 tossed", side1)
        print("Player 2 tossed", side2)
        # Player 1 wins if the coins match
        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print("It's a Match! Player 1 wins a coin.")
         # Player 2 wins if the coins do not match
        else:
            player2.win_coin()
            player1.lose_coin()
            print("No Match! Player 2 wins a coin.")
          # Displays each player's current wallet
        print("\nPlayer 1 has", player1.get_wallet(), "coins.")
        print("Player 2 has", player2.get_wallet(), "coins.")
          # Asks if the user wants to play another round
        play = input("\nDo you want to toss the coins? (y/n): ")
        print("\n--- Final Score ---")
    print("Player 1:", player1.get_wallet())
    print("Player 2:", player2.get_wallet())

    if player1.get_wallet() > player2.get_wallet():
        print("Player 1 wins!")

    elif player2.get_wallet() > player1.get_wallet():
        print("Player 2 wins!")

    else:
        print("It's a draw!")


main()
