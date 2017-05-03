#!~pbui/pub/anaconda2-4.1.1/bin
#MAIN

import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame

#def main():
    #pygame.init()
    #screen = pygame.display.set_mode((800, 800))
    #clock = pygame.time.Clock()

def main(screen):
    screens1.homeScreen(screen)
    pygame.display.flip()

    #mouse click on home screen
    clicked = False
    multiplayer = False
    while not clicked:
		for event in pygame.event.get():
			tupleXY = (0, 0)
			if event.type == pygame.MOUSEBUTTONUP:
				tupleXY = pygame.mouse.get_pos()
			x = tupleXY[0]
			y = tupleXY[1]
			if x >= 50 and x <= 350:
				if y >= 425 and y <= 545:
					clicked = True
					return multiplayer
			if x >= 450 and x <= 750:
				if y >= 425 and y <= 545:
					multiplayer = True
					clicked = True
					return multiplayer

	#return multiplayer

def playGame(multiplayer, screen):
    #play game
    rtn = checkersBoard.playGame(multiplayer)

    #results screen
    if rtn > 0:
		if multiplayer:
			screens1.resultScreen(rtn, screen)
		else:
			screens1.resultScreen(rtn+2, screen)
		pygame.display.flip()
		clicked2 = False
    
        #mouse click on results screen
		while not clicked2:
			for event in pygame.event.get():
				tupleXY = (0, 0)
				if event.type == pygame.MOUSEBUTTONUP:
					tupleXY = pygame.mouse.get_pos()
					x = tupleXY[0]
					y = tupleXY[1]
					if x >= 150 and x <= 650:
						if y >= 450 and y <= 650:
							clicked2 = True
							#checkersBoard.playGame(multiplayer)
							return True
					if x >= 275 and x <= 525:
						if y >= 650 and y <= 750:
							clicked = True
							return False
                if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q] != 0:
					clicked2 = True
					return False

if __name__ == '__main__':
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((800, 800))
	clock = pygame.time.Clock()

	playAgain = True
	while playAgain:
		multiplayer = main(screen)
		playAgain = playGame(multiplayer, screen)
