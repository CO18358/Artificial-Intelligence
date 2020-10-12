#import library to calculate time
import time
#number of solutions
count = 0

#check if the queen can be placed safely
def safety(board, r, c):

    #CHECK COLUMN
    for i in range(r):
        if board[i][c] == 1:
            return False

    #CHECK \ DIAGONAL
    (i, j) = (r, c)
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j - 1

    #CHECK / DIAGONAL
    (i, j) = (r, c)
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i = i - 1
        j = j + 1

    return True

def NQ(board, r):
	#if N queens are placed successfully, print the solution
	if r == N:
		for i in range(N):
			for j in range(N):
				print(board[i][j], end=' ')
			print()
		print()
		global count
		count +=1
		return 
	#try placing queen in ALL columns for every row one by one
	for i in range(N):
		# if no two queens threaten each other
		if safety(board, r, i):
			# place queen
			board[r][i] = 1
			#PROGRESS RECURSIVEL
			NQ(board, r + 1)
			#remove queen upon failure
			board[r][i] = 0

#driver code
print("N-Queen Problem")
N = int(input("Enter the size of board: "))
#INITAL TIME
start = time.time()
board = [[0 for i in range(N)] for j in range(N)]
NQ(board, 0)
#FINAL TIME
end = time.time()
print("Number of solutions: ",count)
print("Program Execution Time: ", end-start, " seconds")

    
