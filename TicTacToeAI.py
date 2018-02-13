import random
import mymod

def columnCoor(grid):
	columnList = []
	for i in range(len(grid)):
		column = []
		for j in range(len(grid[i])):
			column.append(grid[j][i])
		columnList.append(column)
	return columnList

def cornerMidCoor(grid):
	cornerList = []
	isAdd = True
	for i in grid:
		for j in i:
			if isAdd:
				cornerList.append(j)
				isAdd = False
			else:
				isAdd = True
	return cornerList

def isDouble(row, column, diagonal, counter):
	for i in range(len(row)):
		rowCount = 0
		for j in range(len(row[i])):
			if row[i][j] == counter:
				rowCount+=1
			elif row[i][j] != 0:
				break
			else:
				ret = [j, i]
			if rowCount >= 2:
				for k in range(len(row[i])):
					if row[i][k] == 0:
						return k+1, i+1

	for i in range(len(column)):
		columnCount = 0
		for j in range(len(column[i])):
			if column[i][j] == counter:
				columnCount+=1
			elif column[i][j] != 0:
				break
			if columnCount >= 2:
				for k in range(len(column[i])):
					if column[i][k] == 0:
						return i+1, k+1

	diagCount = 0
	for i in range(len(diagonal)):
		if diagonal[i] == counter:
			diagCount += 1
		elif diagonal[i] != 0:
			diagCount = None
			break
	if diagCount >= 2:
		if diagonal[2] == 0:
			return (2, 2)
		elif diagonal[0] == counter:
			return (3, 3)
		elif diagonal[1] == counter:
			return (1, 3)
		elif diagonal[3] == counter:
			return (3, 1)
		elif diagonal[4] == counter:
			return (1, 1)

def winner(row, column, diagonal):
	for x in [1, 2]:	
		if x == 1:
			name = 'Player'
		else:
			name = 'Computer'
		for i in range(len(row)):
			rowCount = 0
			for j in range(len(row[i])):
				if row[i][j] == x:
					rowCount+=1
				if rowCount >= 3:
					return '{} has won!'.format(name)
		for i in range(len(column)):
			columnCount = 0
			for j in range(len(column[i])):
				if column[i][j] == x:
					columnCount+=1
				if columnCount >= 3:
					return '{} has won!'.format(name)
		diagCount = 0
		for i in range(len(diagonal)):
			if diagonal[i] == x:
				diagCount += 1
		if diagCount >= 3 and diagonal[2] == x:
			if diagonal[0] == x and diagonal[4] == x:
				return '{} has won!'.format(name)		
			elif diagonal[1] == x and diagonal[3] == x:
				return '{} has won!'.format(name)

def emptyCoor(grid):
	coorList = []
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j] == 0:
				coorList.append([j+1, i+1])
	print 'empty coordinate list: ', coorList
	return coorList

def AIPick(grid):
	coor = emptyCoor(grid)
	xPick = isDouble(grid, columnCoor(grid), cornerMidCoor(grid), 2)
	yPick = isDouble(grid, columnCoor(grid), cornerMidCoor(grid), 1)
	if xPick:
		return xPick
		#grid[xPick[0]-1][xPick[1]-1] = 2
	elif yPick:
		return yPick
		#grid[yPick[0]-1][yPick[1]-1] = 1
	finalChoice = random.choice(coor)
	return finalChoice
	#grid[finalChoice[0]][finalChoice[1]] = 2

def winner2(grid):
	pass
	# return winner status: X, O, cats, draw
	winner = None
	for row in grid:
		first = row[0]
		if first != 0 and first == row[1] and first == row[2]:
			winner = first
	for colIdx in range(3):
		first = grid[0][colIdx]
		if first != 0 and first == grid[1][colIdx] and first == grid[2][colIdx]:
			winner = first
	# check diagonals
	first = grid[0][0]
	if first != 0 and first == grid[1][1] and first == grid[2][2]:
		winner = first
	first = grid[2][0]
	if first != 0 and first == grid[1][1] and first == grid[0][2]:
		winner = first
	if winner:
		return winner
	#check cat's game

def winIfPossible(grid):
	# return True if moved
	pass

def blockOpponentWin(grid):
	# return True if moved
	pass

def randomMove(grid):
	# return True if moved
	pass

def move(grid):
	if not winIfPossible(grid):
		if not blockOpponentWin(grid):
			randomMove(grid)

		

