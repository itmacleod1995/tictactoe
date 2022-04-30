print("Welcome to the tic tac toe game!\n")
print("----Rules----")
print("The game board is set up as follows")
print("""
    _7_|_8_|_9_
    _4_|_5_|_6_
     1 | 2 | 3
""")

print("Each player picks a digit on their keyboard corresponding to the cell they want to place")
print("Whoever gets three in a row is the winner!")

WINNERCELLS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
selectedSpots = []

board = """
    _7_|_8_|_9_
    _4_|_5_|_6_
     1 | 2 | 3
"""

print(board)

game = False
turn = 1
while game:
    player1 = input("Player 1, choose X or O")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "O"

    if turn % 2 != 0:
        print("Player 1's turn\n")
        chooseAgain = True
        while chooseAgain:
            choice = input("Choose location: ")
            if choice in selectedSpots:
                print("That cell has already been picked! Please pick again ")
            else:
                selectedSpots.append(choice)
    else:
        print("Player 2's turn\n")