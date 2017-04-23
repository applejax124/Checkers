import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame

if __name__ == '__main__':
	screens1.homeScreen()
	#if mouse click in Two Players then display board

	checkersBoard.board(square)

def getClick():
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
			(x, y) = pygame.mouse.get_pos()
			return (x, y)
		else:
			return (0, 0)



if __name__ == '__main__':
	screens1.homeScreen()

	#check if mouse clicks one of the buttons
	clicked = false
	playerNum = 0
	while not clicked:
		x, y = getClick()
		if x >= 25 and x <= 260:
			if y >= 275 and y <= 365:
				playerNum = 1
				clicked = true
		if x >= 325 and x <= 570:
			if y >= 275 and y <= 365:
				playerNum = 2
				clicked = true
	
	#play game
	winner = playGame(playerNum)

	#show win/lose screen 1: P1 Wins, 2: P2 Wins, 3: You win, 4: You lose
	screens1.resultScreen(winner)


