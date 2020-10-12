#import library to calculate time
import time

#function to print the solution
def printboard(n, board):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end='    ')
        print()

#safety function to check if the position is accessible or not  
def safety(board, x, y): 
    if(x >= 0 and y >= 0 and x < n and y < n): 
        if(board[x][y] == -1):
            return True
        return False
 
def KT(n, p, q): 
    # Initialization of Board 
    board = [[-1 for i in range(n)]for i in range(n)] 
      
    # movx and movy: knight's next move 
    movx = [2, 1, -1, -2, -2, -1, 1, 2]
    movy = [1, 2, 2, 1, -1, -2, -2, -1]
      
    # Initial position of the knight
    board[p][q] = 0

    pos = 1
      
    # Check if there exist a possible solution 
    if(not solveKT(n, board, 0, 0, movx, movy, pos)): 
        print("Solution does not exist") 
    else: 
        printboard(n, board) 
  
def solveKT(n, board, curx, cury, movx, movy, pos): 
    if(pos == n**2): 
        return True
      
    # Try all Possible moves from the current location
    for i in range(8): 
        newx = curx + movx[i] 
        newy = cury + movy[i] 
        if(safety(board, newx, newy,)):
            board[newx][newy] = pos 
            if(solveKT(n, board, newx, newy, movx, movy, pos+1)): 
                return True
              
            # Backtracking 
            board[newx][newy] = -1
    return False
          
#driver code
print("N*N board K knights Problem")
n = int(input("Enter the size of board: ")) 
print("Starting point of knight: ")
p = int(input())
q = int(input())
#INITAL TIME
start = time.time()
KT(n, p, q)
#FINAL TIME
end = time.time()
print("Program Execution Time: ", end-start, " seconds")

