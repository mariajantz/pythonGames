import random

def emptyBoard(size):
	return [[0 for i in range(size)] for j in range(size)]


def placeBombs(size, number):
	board = emptyBoard(size)
	for i in range(number):
		x = random.randrange(0, size)
		y = random.randrange(0, size)
		board[y][x] = "x"
	return board

def getAdjacent(board):
	for i in range(len(board)):
		for j in range(len(board)):
			if board[i][j] == "x":
				#add one to all legal surrounding spots
				for k in range(-1, 2):
					for l in range(-1, 2):
						if isLegal(board, i+k, j+l):
							if not (k==-1 and i==0) and not(l==-1 and j==0): #take care of negative indexing
								board[i+k][j+l] += 1
	printBoard(board)

def isLegal(board, row, col):
	try:
		board[row][col]
	except IndexError:
		return False
	if board[row][col] == "x":
		return False
	return True

def printBoard(board):
	for alist in board:
		temp = ""
		for item in alist:
			temp+=(str(item) + " ")
		print(temp)

getAdjacent(placeBombs(5, 5))

''' Output: 
0 1 x 2 x 
0 1 1 2 1 
1 2 2 1 0 
2 x x 1 0 
2 x 3 1 0 
'''