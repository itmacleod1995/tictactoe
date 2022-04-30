print("Welcome to the tic tac toe game!\n")
print("----Rules----")
print("The game board is set up as follows")
print("""
    _7_|_8_|_9_
    _4_|_5_|_6_
     1 | 2 | 3
""")

print("Each player picks a digit on their keyboard corresponding to the cell they want to place")
print("Whoever gets three in a row is the winner!\n")

WINNERCELLS = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]
selectedSpots = []

player1Cells = []
player2Cells = []

board = """
    _7_|_8_|_9_
    _4_|_5_|_6_
     1 | 2 | 3
"""


def makeChoice(player, b, playerNum):
    """Function that allows the player to play their piece on the board"""
    chooseAgain = True
    while chooseAgain:
        choice = input()
        if choice in selectedSpots:
            print("That cell has already been picked! Please pick again ")
        else:
            selectedSpots.append(choice)
            if playerNum == 1:
                player1Cells.append(choice)
            else:
                player2Cells.append(choice)
            updatedboard = b.replace(choice, player)
            print(updatedboard)
            chooseAgain = False

        return updatedboard

def checkIfThreeInARow(selectedSpots, winningcells):
    """Method that checks if the player has gotten three in a row"""
    count = 0
    for cell in winningcells:
        for num in cell:
            if str(num) not in selectedSpots:
                count = 0
                break
            elif str(num) in selectedSpots:
                count += 1
                if count == 3:
                    return True
    return False



game = True
turn = 1
player1 = input("Player 1, choose X or O: ")

"""Game Loop"""
while game:
    print("")
    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    if turn % 2 != 0:
        print("Player 1, choose location: ", end="")
        board = makeChoice(player1, board, 1)
        if checkIfThreeInARow(selectedSpots=player1Cells, winningcells=WINNERCELLS):
            print("Three in a row! Player 1 wins!")
            game = False
    else:
        print("Player 2, choose location: ", end="")
        board = makeChoice(player2, board, 2)
        if checkIfThreeInARow(selectedSpots=player2Cells, winningcells=WINNERCELLS):
            print("Three in a row! Player 2 wins!")
            game = False

    if len(selectedSpots) == 9:
        print("Tie!")
        game = False

    turn += 1