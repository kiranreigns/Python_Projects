import random
board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

currentPlayer = 'X'
winner = None
gameRunning = True

# print the board
def printBoard(board):
    print("\n")
    print(f"     1   2   3")
    print("   +---+---+---+")
    print(f" 1 | {board[0]} | {board[1]} | {board[2]} |")
    print("   +---+---+---+")
    print(f" 2 | {board[3]} | {board[4]} | {board[5]} |")
    print("   +---+---+---+")
    print(f" 3 | {board[6]} | {board[7]} | {board[8]} |")
    print("   +---+---+---+")
    print("\n")


# take player input
def playerInput(board):
    while True:
        try:
            inp = int(input("Enter a number 1-9: "))
            if inp < 1 or inp > 9:
                print("Please enter a number between 1 and 9!")
                continue
                
            if board[inp-1] == " ":
                board[inp-1] = currentPlayer
                break
            else:
                print("Oops! That spot is already occupied. Try again!")
        except ValueError:
            print("Please enter a valid number!")

# check for the win or tie
def checkRows(board):
    global winner
    if board[0] ==  board[1] == board[2] and board[1] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != " ":
        winner = board[4]
        return True
    elif board[6] == board[7] == board[8] and board[7] != " ":
        winner = board[7]
        return True 
    
def checkCols(board):
    global winner
    if board[0] ==  board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[2]
        return True 
    
def checkDiag(board):
    global winner
    if board[0] ==  board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != " ":
        winner = board[2]
        return True
    
def checkTie():
    global gameRunning
    if " " not in board:
        gameRunning = False
        print("It's a tie!")
        
def checkWin():
    global gameRunning
    if checkRows(board) or checkCols(board) or checkDiag(board):
        gameRunning = False
        print(f"Player {winner} wins!")
        
# switch the players
def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = "O"
    else:
        currentPlayer = "X"
# Computer move
def computer(board):
    while currentPlayer == 'O':
        pos = random.randint(0,8)
        if board[pos] == " ":
            board[pos] = 'O'
            switchPlayer()


while gameRunning:
    printBoard(board)
    checkWin()
    checkTie()
    if not gameRunning:  
        break
    playerInput(board)
    switchPlayer()
    computer(board)
