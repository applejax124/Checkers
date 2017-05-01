#!~pbui/pub/anaconda2-4.1.1/bin
#MAIN

import screens1
import checkersBoard
import findCell
import classes
import gameplay
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()

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
		if x >= 450 and x <= 750:
		    if y >= 425 and y <= 545:
			multiplayer = True
			clicked = True


    #play game
    rtn = checkersBoard.playGame(multiplayer)

    #results screen
    if 1 > 0:
        screens1.resultScreen(1, screen)
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
                            main()
                if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q] != 0:
                    clicked2 = True

if __name__ == '__main__':
    main()
