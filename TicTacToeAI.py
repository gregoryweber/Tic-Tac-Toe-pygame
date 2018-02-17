#After 2 weeks in development, I present, the almost perfect tic tac toe AI that's only 83 lines!!!! (formerly more than 120)

import random #for random picking

def pickThird(grid, counter): #picks the third coordinate for the three in a row
	for i in ['row', 'column', 'leftDiag', 'rightDiag']: #cycles through all possible three in a row cases
		thirdCoor = check3Cells(grid, i, counter) #checks to see if there is a 2 in a row
		if thirdCoor: #if there is a two in a row...
			return thirdCoor #return the third coordinate
	return None #if there is no third coordinate, return none

def check3Cells(grid, type2, counter): #checks to see if there is a three in a row and returns one
	for i in range(3):  #goes through the rows
		count = 0 #the count of how many of a counter there is
		for j in range(3): #goes through the columns
			if type2 == 'row': # if the type is a row
				gridType = grid[i][j] #set the type to go through each unit one by one
				coorPass = [i, j] #set the passed coordinates to be row, column
			elif type2 == 'column': #if its a column, check by the reverse and return the reverse
				gridType = grid[j][i]
				coorPass = [j, i]
			elif type2 == 'leftDiag': #if its the left diagonal, check it and return it
				gridType = grid[j][j]
				coorPass = [j, j]
			elif type2 == 'rightDiag': #if its the right diagonal, check it and return it
				gridType = grid[j][2-j]
				coorPass = [j, 2-j]

			if gridType == counter: #if the cell is equal to the counter piece, add one to the counter count
				count+=1
			elif gridType != 0: #if ts equal to another counter piece, there cant be a two in a row
				count = 0
				break
			else: #if there is a zero, then store the value for returning if there is a two in a row
				ret = coorPass #stores the zero value
		if count == 2: #if there are two of the same counter in a row...
			return ret #then return the stored zero value

def AIPick(grid): #finally picks what cell to go to and changes the grid cell
	offensivePick = pickThird(grid, 2) #the offensive pick, if there is one
	defensivePick = pickThird(grid, 1) #the defensive pick, if there is one
	if offensivePick: #if there is a pick that will win the game, pick it
		grid[offensivePick[0]][offensivePick[1]] = 2
	elif defensivePick: #if there is a pick which will block the opponent, pick it
		grid[defensivePick[0]][defensivePick[1]] = 2
	else: #if there is no 2 in a row, then randomly pick
		randRow = random.randint(0, 2) #a random row pick
		randColumn = random.randint(0, 2) #a random column pick
		while grid[randRow][randColumn] != 0: #while the selected cell is not empty, keep picking
			randRow = random.randint(0, 2)
			randColumn = random.randint(0, 2)

		grid[randRow][randColumn] = 2 #sets the selected empty grid cell to an x

def isWinner(grid): #returns who won the game, if there is a winner
	winner = None #winner starts out as none
	for row in grid: #goes through the rows of the grid
		first = row[0] #the first element of the row
		if first != 0 and first == row[1] and first == row[2]: #if the first row element is equal throughout the entire row...
			winner = first #then the winner is the first element
	for colIdx in range(3): #goes through the columns
		first = grid[0][colIdx] #the first element of each column
		if first != 0 and first == grid[1][colIdx] and first == grid[2][colIdx]: #if the first column element is equal throughout the entire column...
			winner = first

	first = grid[0][0]
	if first != 0 and first == grid[1][1] and first == grid[2][2]: #goes through the case of a left diagonal
		winner = first
	first = grid[2][0]
	if first != 0 and first == grid[1][1] and first == grid[0][2]: #goes through the case of a right diagonal
		winner = first
	if winner: #if there is a winner...
		return winner  #return it

	isFull = True #checks to see if the grid is full for cat's game
	for row in grid: #goes through the row of the grid
		for column in row: #goes through the column of the grid
			if column == 0: #if any cell is empty, then the grid can't be full
				isFull = False
	if isFull: #if it is full, the grid must be in a cat's game
		return 'tie' #return tie
	else: #if it isn't full and no one has won, then no one has won
		return False