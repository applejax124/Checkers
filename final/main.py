#!~pbui/pub/anaconda2-4.1.1/bin
#MAIN

import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame

def home(screen):
    screens1.homeScreen(screen)
    pygame.display.flip()

    #mouse click on home screen
    clicked = False
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
			return 1
		if x >= 450 and x <= 750:
		    if y >= 425 and y <= 545:
			multiplayer = True
			clicked = True
			return 2
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q] != 0:
                clicked = True
                return 0

def results(mode, screen):

    #display results screen
    if mode == 2:
        screens1.resultScreen(rtn, screen)
    elif mode == 1:
        screens1.resultScreen(rtn+2, screen)
	pygame.display.flip()
	clicked = False

    #wait for a button press
    while not clicked:
        for event in pygame.event.get():
            tupleXY = (0, 0)
	    if event.type == pygame.MOUSEBUTTONUP:
	        tupleXY = pygame.mouse.get_pos()
	        x = tupleXY[0]
	        y = tupleXY[1]
	        if x >= 150 and x <= 650 and y >= 450 and y <= 650: #play again button
	            return True
		if x >= 275 and x <= 525 and y >= 650 and y <= 750: #quit button
		    return False

if __name__ == '__main__':
	#initialize pygame
	pygame.init()
	pygame.font.init()
	screen = pygame.display.set_mode((800, 800))
	clock = pygame.time.Clock()

	playGame = True
	while playGame:

		#display homescreen
		mode = home(screen)

		#quits if q is pressed on homescreen
		if mode == 0: 
			playGame = False
			continue

		#play game
		rtn = checkersBoard.playGame(mode)
		#quits if quit button is pressed
		if rtn == 0:
			playGame = False
			continue

		#display results screen if quit button not pressed
		else:
			playGame = results(mode, screen)
