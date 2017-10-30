#sudoku solving with backtracking
solutions=False
several=False

def backtrack(grid):
	global solutions
	global several
	next = findUnassigned(grid)
	#print(next)
	if not next:
		#print(grid)
		if solutions == False:
			solutions=True
			return False
		else:
			print("hello again")
			several=True 
			return True #This way we find out if there is more than one solution, then stop
	#pick a solution, continue to try examples
	for i in range(len(grid)):
		if isAllowed(grid, next, i+1):
			grid[next[0]][next[1]] = i+1
			if backtrack(grid):
				return True
			grid[next[0]][next[1]] = 0
	return False


def isAllowed(grid, loc, num):
	row, col = loc
	if not inRow(grid, row, num):
		if not inCol(grid, col, num):
			if not inBox(grid, loc, num):
				return True
	return False

def inRow(grid, row, num):
	if num in grid[row]:
		return True
	return False

def inCol(grid, col, num):
	for i in range(len(grid)):
		if num == grid[i][col]:
			return True
	return False

def inBox(grid, loc, num):
	row, col = loc
	boxsize = int(len(grid)**.5)
	for i in range(-int(row%boxsize), -int(row%boxsize)+boxsize, 1):
		for j in range(-int(col%boxsize), -int(col%boxsize)+boxsize, 1):
			if grid[row+i][col+j] == num:
				return True
	return False

def findUnassigned(grid):
	for i in range(len(grid)):
		for j in range(len(grid)):
			if grid[i][j] == 0:
				return [i, j]

agrid = [[1, 0, 0, 3], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]] #2D array, need to have numbers 1-3 in each row and col
#backtrack(agrid)

#[[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]

#now the methods for generation

def emptyGrid(size):
	return [[0 for i in range(size)] for j in range(size)]

import random

def generate(size, grid = emptyGrid(4)):
	global solutions
	global several
	y = random.randrange(size)
	x = random.randrange(size)
	num = random.randrange(1, size+1)
	if grid[y][x] == 0:
		#will need another if statement here
		grid[y][x] = num
		print(grid)
		backtrack(grid)
		if solutions:
			print("bye")
			solutions=False #set back to default so we can rerun it.
			#place another random one. 
			print("hm")
			if several:
				print("hello")
				several=False
				#this doesn't work because it's apparently passing a pointer, not a new grid.
				generate(size, grid)

	print(grid)

generate(4)





