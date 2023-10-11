import random
board = ["---", "---",'---',
         "---", "---",'---',
         "---", "---",'---']
currentPlayer = " X "
winner = None
gameRunning = True

# printing the game board
def printBoard(board):
    print("-------------")
    print("|" + board[0] + "|" + board[1]+ "|" + board[2] + "|")
    print("-------------")
    print("|" + board[3] + "|" + board[4]+ "|" + board[5] + "|")
    print("-------------")
    print("|" + board[6] + "|" + board[7]+ "|" + board[8] + "|")
    print("-------------")
    

# take player input
def playerInput(board):
    player_input = int(input("Select a spot 1-9..."))
    if player_input >= 1 and player_input <= 9 and board[player_input - 1] == "---":
        board[player_input - 1] = currentPlayer
    else:
        print("Oops, the spot is already occupied!")


# check for win or tie
# check if the symbols in the rows are same or not
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0]!= "---":
        winner = board[0]
        return True
    elif board[3] == board[4] ==board[5] and board[3]!= "---":
        winner = board[3]
        return True
    elif board[6] == board[7]== board[8] and board[6]!= "---":
        winner = board[6]
        return True
# check if the symbols in the column are same or not
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "---":
        winner = board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1]!= "---":
        winner = board[1]
        return True
    elif board[2] == board[5]== board[8] and board[2]!= "---":
        winner = board[2]
        return True
# check if the symbols in the diagonal are same or not
def checkDiagonal(board):
    global winner
    if board[2] == board[4] == board[6] and board[4]!= "---":
        winner = board[2]
        return True
    elif board[0] == board[4] ==board[8] and board[0]!= "---":
        winner = board[0]
        return True

# check for win 
def checkIfWin(board):
    global gameRunning
    if checkHorizontal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkVertical(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiagonal(board):
        printBoard(board)
        print(f"The winner is {winner}!")
        gameRunning = False
   
# check if the game is tied
def checkIfTie(board):
    global gameRunning
    if "---" not in board:
        printBoard(board)
        print("It is a tie!")
        gameRunning = False

# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == " X ":
        currentPlayer = " O "
    else: 
        currentPlayer = " X "

# computer
def computer(board):
    while currentPlayer == " O ":
        position =random.randint(0,8)
        if board[position] == "---":
            board[position] = " O "
            switchPlayer()

# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkIfWin(board)
    checkIfTie(board)
    switchPlayer()
    computer(board)
    checkIfWin(board)
    checkIfTie(board)