# Subtract a Square Game
#
#
#
# Explanation:
#
# 2 Players have a pile of 50 coins between them.
# They have to subtract a square number of coins (1, 4, 9, etc) such that the remaining coins are not negative. 
# When the number of coins reaches 0, the game ends and the last player to subtract wins the game.
#
#
# Good luck and have fun :D

from math import sqrt

#   Contains all the global data for the game
gameData = {
    "coins": 50,
    "turn": 0,
    "done": False
}

#   Handles the winning player message
def winner(player):
    print("Player "+ player + " wins!")
    gameData["done"] = True
    input("Press enter to exit...")

#   Processes the moves
def subSquare(n, player):
    gameData["coins"] -= n;

    if gameData["coins"] == 0:
        winner(player)

    else:
        gameData["turn"] += 1

#   Main function
def main():

    #   Runs until game is over
    while not gameData["done"]:
        print("Coins: " + str(gameData["coins"]))

        #   If it is an even turn, then it is player one's turn and if it an odd turn it is player two's turn
        player = "1" if gameData["turn"] % 2 == 0 else "2"

        n = int(input("Player "+ player + " enter a number: "))

        #   Check if the number is a square and that it is less than the number of coins
        if sqrt(n) ** 2 == n and n <= gameData["coins"]:
            subSquare(n, player)
        else:
            print("Number is too big or not a square. Please try again\n")

main()