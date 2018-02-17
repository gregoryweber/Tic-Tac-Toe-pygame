#Gregory Weber
#Week 19
#Tic Tac Toe (with AI)

import pygame #for user interface and display
import TicTacToeAI #all the functions for the AI
import time #for waiting for the AI turn

WIDTH = 800 #the width of the screen
HEIGHT = 500 #the height of the screen
COUNTER_SIZE = int(1.0/3.0*WIDTH)/3 - 25 #the size of the counter, which is determined based of the width
COUNTER_STROKE_SIZE = 5 #the stroke size of the x's and o's
LINE_THICKNESS = 4 #the thickness of the grid lines
LINE_COLOR = [0, 0, 0] #the color of the grid lines
BACKGROUND_COLOR = [255, 255, 255] #the background color of the screen
CIRCLE_COLOR = [0, 200, 0] #the color of the circle
X_COLOR = [200, 0, 0] #the color of the x
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

def userPick(pos, grid): #draws the counter on the screen
	gridCoor = gridPosition(pos) #the grid coordinates that the circle is in
	gridX = gridCoor[0]-1 #the x coordinate of the cell
	gridY = gridCoor[1]-1 #the y coordinate of the cell
	grid[gridY][gridX] = 1 #makes sure to fill the empty cell

def isCellEmpty(pos, grid): #checks to see if the selected cell is empty
	gridCoor = gridPosition(pos) #gets the grid coordinates of the position
	return grid[gridCoor[1]-1][gridCoor[0]-1] == 0 #returns true or false if the cell is empty

def resetBackground(screen): #resets the bakground
	screen.fill([255, 255, 255]) 
	for i in range(1, 3): #draws the grid lines
		pygame.draw.line(screen, LINE_COLOR, [1.0/3.0*WIDTH*i, 0], [1.0/3.0*WIDTH*i, HEIGHT], LINE_THICKNESS)
		pygame.draw.line(screen, LINE_COLOR, [0, 1.0/3.0*HEIGHT*i], [WIDTH, 1.0/3.0*HEIGHT*i], LINE_THICKNESS)	

def drawText(textValue, screen): #draws the text onto the screen
	FONT = pygame.font.SysFont(None, 70) #the font of the text
	if textValue == 1: #if the player has won, player wins
		message = 'Player has won!'
	elif textValue == 2: #else if the computer has won, computer wins
		message = 'Computer has won!'
	else: #otherwise must be cat's game
		message = "Cat's game!"
	text = FONT.render(message, True, (0, 255, 255)) #sets the text
	shadow = FONT.render(message, True, (0, 0, 0, 0)) #sets the shadow
	textRect = text.get_rect(center=(WIDTH/2, HEIGHT/2)) #puts the center of the text onto the center of screen
	shadowRect = text.get_rect(center=(WIDTH/2-5, HEIGHT/2+5)) #puts the center of the shadow onto the center of the screen
	screen.blit(shadow, shadowRect) #blits the text 
	screen.blit(text, textRect) #blits the shadow

def draw(screen, grid): #takes in the grid, and draws the screen
	resetBackground(screen)
	rowCount = 0 #the row of the grid
	for row in grid: #checks each value in the grid 
		rowCount+=1
		colCount=0 #the column of the grid
		for val in row: #checks each value in each list of the grid
			colCount+=1
			if val == 1: #if the value is a 1, draw a circle
				drawCircle(screen, [colCount, rowCount])
			elif val == 2: #if the value is a 2, draw a circle
				drawX(screen, [colCount, rowCount])

	winner = TicTacToeAI.isWinner(grid) #either a value of 1, 2, 'tie', none, or false, whatever the winner is
	if winner: #if there is a winner, draw the text saying so
		drawText(winner, screen)
	pygame.display.flip()

def isGameOver(grid): #determines if the game is over
	return TicTacToeAI.isWinner(grid) != False #returns true or false if there is a winner

def main(): #the main program
	isUserTurn = True #determines whose turn it is
	pygame.init() #initiate pygame
	screen = pygame.display.set_mode([WIDTH, HEIGHT]) #the screen
	draw(screen, gridState)
	running = True #allows while loop to run
	while running: #repeats the program
		for event in pygame.event.get(): #goes through all the events in pygame
			if event.type == pygame.QUIT: #if one of those events is a quit, then quit
				running = False
			elif event.type == pygame.MOUSEBUTTONDOWN: #if one of those events is a mouse click
				mousePos = pygame.mouse.get_pos() #gets mouse position
				if isUserTurn and isGameOver(gridState) == False:
					if isCellEmpty(mousePos, gridState): #if the selected cell is empty, pick it
						userPick(mousePos, gridState) #draws a counter on the screen at the mouse position
						draw(screen, gridState)
						isUserTurn = False
				if isUserTurn == False and isGameOver(gridState) == False: #if its the AI's turn, and its not game over
					time.sleep(1)
					TicTacToeAI.AIPick(gridState)
					draw(screen, gridState)
					isUserTurn = True

if __name__ == '__main__': #if this program is being run from this script, then run the program
	main()

