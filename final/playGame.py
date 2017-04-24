#!~pbui/pub/anaconda2-4.1.1/bin

import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame


#if __name__ == '__main__':
#	pygame.init()
#	swidth = 800
#	sheight = 800

#	screen = pygame.display.set_mode((swidth, sheight))
#	clock = pygame.time.Clock()
	#done = False


#	screens1.homeScreen(screen)
	#if mouse click in Two Players then display board

	#checkersBoard.board(square)

def getClick():
	for event in pygame.event.get():
		tupleXY = (0, 0);
		if event.type == pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
			tupleXY = pygame.mouse.get_pos()
			return tupleXY


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	clock = pygame.time.Clock()

	screens1.homeScreen(screen)

	#check if mouse clicks one of the buttons
	clicked = False
	playerNum = 0
	while not clicked:
		for event in pygame.event.get():
			tupleXY = (0, 0)
			if event.type == pygame.MOUSEBUTTONUP:
				tupleXY = pygame.mouse.get_pos()
				x = tupleXY[0]
				y = tupleXY[1]
		#tupleXY = getClick()
		#x = tupleXY[0]
		#y = tupleXY[1]
				if x >= 50 and x <= 350:
					if y >= 425 and y <= 545:
						playerNum = 1
						pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(50, 50, 50, 50))
						clicked = True
				if x >= 450 and x <= 750:
					if y >= 425 and y <= 545:
						playerNum = 2
						pygame.draw.rect(screen, (50, 50, 50), pygame.Rect(300, 300, 50, 50))
						clicked = True


	#play game
	#winner = checkersBoard.playGame(playerNum, screen)
	#show win/lose screen 1: P1 Wins, 2: P2 Wins, 3: You win, 4: You lose
	#screens1.resultScreen(winner)


