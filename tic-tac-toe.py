# TicTacToe using minimax

# Game Board
def Gameboard(board):
    print()
    for i in range(0, 9):
        if((i > 0) and ((i % 3) == 0)):
            print()
        if(board[i] == 0):
            print("---", end=" ")
        if (board[i] == 1):
            print(" X ", end=" ")
        if(board[i] == -1):
            print(" O ", end=" ")
    print()
    print()

# Player X
def x_move(board):
    loc = int(input("Enter a number between 1-9 to place X : "))
    while(board[loc-1] != 0):
        print("Invalid Move! Try again!")
        loc = int(input("Enter a number between 1-9 to place X : "))
    board[loc-1] = 1

# Player O
def o_move(board):
    loc = int(input("Enter a number between 1-9 to place O : "))
    while(board[loc-1] != 0):
        print("Invalid Move! Try again!")
        loc = int(input("Enter a number between 1-9 to place O : "))
    board[loc-1] = -1

# Win conditions
def condition(board):
    win = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
               [0, 3, 6], [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]

    for i in range(0, 8):
        if(board[win[i][0]] != 0 and
           board[win[i][0]] == board[win[i][1]] and
           board[win[i][0]] == board[win[i][2]]):
            return board[win[i][2]]
    return 0

# Minimax


def minimax(board, player):
    a = condition(board)
    if(a != 0):
        return (a*player)
    loc = -1
    value = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = player
            score = -minimax(board, (player*-1))
            if(score > value):
                value = score
                loc = i
            board[i] = 0

    if(loc == -1):
        return 0
    return value

# Computer Turn using Minimax
def comp(board):
    loc = -1
    value = -2
    for i in range(0, 9):
        if(board[i] == 0):
            board[i] = 1
            score = -minimax(board, -1)
            board[i] = 0
            if(score > value):
                value = score
                loc = i

    board[loc] = 1

# Player vs. Computer mode
def pvc(board):
    print()
    print("Computer : X Vs. You : O")
    player = int(input("Enter to play 1st or 2nd: "))
    for i in range(0, 9):
        if(condition(board) != 0):
            break
        if((i+player) % 2 == 0):
            comp(board)
        else:
            Gameboard(board)
            o_move(board)

# Player vs. Player mode
def pvp(board):
    for i in range(0, 9):
        if(condition(board) != 0):
            break
        if((i) % 2 == 0):
            Gameboard(board)
            x_move(board)
        else:
            Gameboard(board)
            o_move(board)

def winner(board):
    x = condition(board)
    if(x == 0):
        Gameboard(board)
        print("The Game is a Draw!")
        print()
    if(x == 1):
        Gameboard(board)
        print("Player X wins the Game!")
        print()
    if(x == -1):
        Gameboard(board)
        print("Player O wins the Game!")
        print()


# Driver Code
print("====================")
print("TIC-TAC-TOE using AI")
print("====================")

board = [
            0, 0, 0,
            0, 0, 0,
            0, 0, 0,
        ]

print("\n1. Player vs. Computer \n2. Player vs. Player")
op = int(input("Select the Game Mode: "))
if(op == 1):
    pvc(board)
else:
    pvp(board)

winner(board)
