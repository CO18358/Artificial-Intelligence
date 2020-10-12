# import library to calculate time
import time
# number of solutions
count = 0

# print board
def printboard(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

# Find max no. of knights that can be placed
def maxK(row, col):

    # If row or column is 1
    if (row == 1 or col == 1):

        # If yes, then simply print total blocks
        return max(row, col)

    # If row or column is 2
    elif (row == 2 or col == 2):

        # If yes, then simply calculate consecutive 2 rows or columns
        k = 0
        k = (max(row, col) // 4) * 4

        if (max(row, col) % 4 == 1):
            k += 2

        elif (max(row, col) % 4 > 1):
            k += 4

        return k

    # For general case, just print the half of total blocks
    else:
        return (((row * col) + 1) // 2)

# mark unsafe place on board
def mark(board, row, col, i, j):

	if((i+2) < row and (j-1) >= 0):
		board[i+2][j-1]=0

	if((i-2) >= 0 and (j-1) >= 0):
		board[i-2][j-1]=0

	if((i+2) < row and (j+1) < col):
		board[i+2][j+1]=0

	if((i-2) >= 0 and (j+1) < col):
		board[i-2][j+1]=0

	if((i+1) < row and (j+2) < col):
		board[i+1][j+2]=0

	if((i-1) >= 0 and (j+2) < col):
		board[i-1][j+2]=0

	if((i+1) < row and (j-2) >= 0):
		board[i+1][j-2]=0

	if((i-1) >= 0 and (j-2) >= 0):
		board[i-1][j-2]=0

# check safe place on board
def canplace(board, i, j):
	if(board[i][j]=='-'):
		return True
	else:
		return False

# place 1 Knight on a board
def place(board, new_board, i, j):
	for a in range(N):
		for b in range(N):
			new_board[a][b] = board[a][b]
	
	new_board[i][j]=1
	mark(new_board, N, N, i, j)

# place K knights on board
def NK(board, row, col, x, y, K):
	if( K == 0 ):
		printboard(board)
		print()
		global count
		count += 1
	else:

		# Loop to check all places
		for i in range(x,row):
			for j in range(y, col):

				# check safety of block
				if(canplace(board, i, j)):

					# Create new board and place a knight
					new_board = [['-' for i in range(N)] for j in range(N)]
					place(board, new_board, i, j)

					# Recursivey call function for Remaining Knights
					NK(new_board, N, N, i, j, K-1)
					del new_board
			y = 0

# driver code
print("K-knights Problem")
N = int(input("Enter the size of board: "))
board = [['-' for i in range(N)] for j in range(N)]
#INITAL TIME
start = time.time()
#no. of max Knights possible
K = maxK(N, N)
NK(board, N, N, 0, 0, K)
#FINAL TIME
end = time.time()
print("Number of solutions: ",count)
print("Program Execution Time: ", end-start, " seconds")