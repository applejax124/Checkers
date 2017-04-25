#!~pbui/pub/anaconda2-4.1.1/bin

import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame


if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((800, 800))
	clock = pygame.time.Clock()

        #print "homescreen should come up"
	screens1.homeScreen(screen)
        pygame.display.flip()
        #print "after homescreen"

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
				if x >= 50 and x <= 350:
					if y >= 425 and y <= 545:
						playerNum = 1
						clicked = True
				if x >= 450 and x <= 750:
					if y >= 425 and y <= 545:
						playerNum = 2
						clicked = True


	#play game
        checkersBoard.playGame(2)
	#show win/lose screen 1: P1 Wins, 2: P2 Wins, 3: You win, 4: You lose
	screens1.resultScreen(1, screen)


