#Gregory Weber
#Week 19
#Pygame

import pygame #for user interface and display
import TicTacToeAI
import time
WIDTH = 800 #the width of the screen
HEIGHT = 500 #the height of the screen
COUNTER_SIZE = int(1.0/3.0*WIDTH)/3 - 25 #the size of the counter, which is determined based of the width
COUNTER_STROKE_SIZE = 5 #the stroke size of the x's and o's
LINE_THICKNESS = 4 #the thickness of the grid lines
LINE_COLOR = [0, 0, 0] #the color of the grid lines
BACKGROUND_COLOR = [255, 255, 255] #the background color of the screen
CIRCLE_COLOR = [0, 200, 0] #the color of the circle
X_COLOR = [200, 0, 0] #the color of the x
clickState = 0
gridState = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] #the state of the grid

def drawX(screen, gridCoor): #function which draws an x at a specified grid coordinates
	coor = modelToScreenCoor(gridCoor)  #converts the grid coordinates to screen coordinates
	pygame.draw.line(screen, X_COLOR, [coor[0]+COUNTER_SIZE, coor[1]+COUNTER_SIZE], [coor[0]-COUNTER_SIZE, coor[1]-COUNTER_SIZE], COUNTER_STROKE_SIZE)
	pygame.draw.line(screen, X_COLOR, [coor[0]+COUNTER_SIZE, coor[1]-COUNTER_SIZE], [coor[0]-COUNTER_SIZE, coor[1]+COUNTER_SIZE], COUNTER_STROKE_SIZE)

def drawCircle(screen, gridCoor): #draws a circle at a specified grid coordinates
	coor = modelToScreenCoor(gridCoor) #gets screen coordinates from grid coordinates
	pygame.draw.circle(screen, CIRCLE_COLOR, coor, COUNTER_SIZE, COUNTER_STROKE_SIZE)

def isInSect(pos, x1, y1, x2, y2): #returns true if the inputed position is in the specified x and y coordinates
	return pos[0] <= x1 and pos[1] <= y1 and pos[0] >= x2 and pos[1] >= y2

def gridPosition(pos): #returns the grid coordinates of a specified position
	for i in range(1,4): #checks the three columns
		for j in range(1,4): #checks the three rows
			if isInSect(pos, 1.0/3.0*WIDTH*j, 1.0/3.0*HEIGHT*i, 1.0/3.0*WIDTH*(j-1), 1.0/3.0*HEIGHT*(i-1)): #if the inputed position is inside a sector...
				return j,i #return the grid coordinates

def modelToScreenCoor(gridPos): #translates the grid coordinates into actual screen coordinates 
	return [int(1.0/3.0*WIDTH*gridPos[0]-1.0/6.0*WIDTH), int(1.0/3.0*HEIGHT*gridPos[1]-1.0/6.0*HEIGHT)] #returns a value in the middle of a sector

def drawCounter(screen, pos, grid): #draws the counter on the screen
	global clickState
	gridCoor = gridPosition(pos) #the grid coordinates that the circle is in
	gridX = gridCoor[0]-1 #the x coordinate of the cell
	gridY = gridCoor[1]-1 #the y coordinate of the cell
	if grid[gridY][gridX] == 0: #checks to see if the appropriate cell is empty
		clickState = flip(clickState)
		if clickState == 1: #if the state is circle
			drawCircle(screen, gridCoor) 
			grid[gridY][gridX] = 1 #makes sure to fill the empty cell
		else: #if the state isnt circle, draw an x
			drawX(screen, gridCoor)
			grid[gridY][gridX] = 2

def drawAICounter(screen, pos, grid):
	global clickState
	print 'ai position: ', pos
	gridX = pos[0]-1
	gridY = pos[1]-1
	print 'aipickx: ', gridX
	print 'aipicky: ', gridY
	if grid[gridY][gridX] == 0: #checks to see if the appropriate cell is empty
		clickState = flip(clickState)
		if clickState == 1: #if the state is circle
			drawCircle(screen, pos) 
			grid[gridY][gridX] = 1 #makes sure to fill the empty cell
		else: #if the state isnt circle, draw an x
			drawX(screen, pos)
			grid[gridY][gridX] = 2

def flip(state): #flips the state from 0 (circle) to 1 (x)
	if state == 0: #flips it to 1
		 state = 1
	else: #flips it to 0
		state = 0
	return state

def resetBackground(screen): #resets the bakground
	screen.fill([255, 255, 255]) 
	for i in range(1, 3): #draws the grid lines
		pygame.draw.line(screen, LINE_COLOR, [1.0/3.0*WIDTH*i, 0], [1.0/3.0*WIDTH*i, HEIGHT], LINE_THICKNESS)
		pygame.draw.line(screen, LINE_COLOR, [0, 1.0/3.0*HEIGHT*i], [WIDTH, 1.0/3.0*HEIGHT*i], LINE_THICKNESS)	

def isGridFull(grid): #checks to see if the grid is full of tokens
	isFull = [] #list of cell values, either true or false
	for x in grid: #goes through all values in grid
		for i in x: #goes through all values in the values of grid
			if i == 0: #if empty, append that its empty
				isFull.append(False)
			else: #if cell is not empty append that it is full
				isFull.append(True)
	return all(isFull) #if all cells are full, return true

def draw(screen, grid, isUserTurn):
  resetBackground()
  for row in grid:
    for val in row:
      if val == 1:
      	drawCircle(screen, [row, col])
      elif val == 2:
      	drawX(screen, [row, col])
  if isWinner(grid):
  	drawWinnerText()
  elif isCatsGame():
  	drawCatsGameText()
  elif isUserTurn:
  	drawUserTurnText()
  pygame.flip()


def main(): #the main program
	gameEnd = False
	pygame.init() #initiate pygame
	pygame.display.set_caption('Tic Tac Toe')
	FONT = pygame.font.SysFont(None, 70)
	screen = pygame.display.set_mode([WIDTH, HEIGHT]) #the screen
	resetBackground(screen) #resets the background with grid lines
	pygame.display.flip()
	running = True #allows while loop to run
	while running: #repeats the program
		for event in pygame.event.get(): #goes through all the events in pygame
			if event.type == pygame.QUIT: #if one of those events is a quit, then quit
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN and gameEnd == False: #if one of those events is a mouse click
				mousePos = pygame.mouse.get_pos() #gets mouse position					
				drawCounter(screen, mousePos, gridState) #draws a counter on the screen at the mouse position
				pygame.display.flip()
				winner = TicTacToeAI.winner(gridState, TicTacToeAI.columnCoor(gridState), TicTacToeAI.cornerMidCoor(gridState))
				if winner:
					text = FONT.render(winner, True, (0, 153, 255))
					textRect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
					screen.blit(text, textRect)
					gameEnd = True
				elif isGridFull(gridState):
					text = FONT.render('Tie!', True, (0, 153, 255))
					textRect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
					screen.blit(text, textRect)
					gameEnd = True
				if gameEnd == False:
					secondPick = TicTacToeAI.AIPick(gridState)
					print 'second pick: ', secondPick
					time.sleep(1)
					drawAICounter(screen, secondPick, gridState)
				winner = TicTacToeAI.winner(gridState, TicTacToeAI.columnCoor(gridState), TicTacToeAI.cornerMidCoor(gridState))
				if winner:
					text = FONT.render(winner, True, (0, 153, 255))
					textRect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
					screen.blit(text, textRect)
					gameEnd = True
				elif isGridFull(gridState):
					text = FONT.render('Tie!', True, (0, 153, 255))
					textRect = text.get_rect(center=(WIDTH/2, HEIGHT/2))
					screen.blit(text, textRect)
					gameEnd = True
				pygame.display.flip()

if __name__ == '__main__': #if this program is being run from this script, then run the program
	main()