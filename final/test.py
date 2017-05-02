#!/pbui/pub/anaconda2-4.1.1/bin

#results screen testing

import screens1
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()

screens1.resultScreen(4, screen)
pygame.display.flip()

clicked = False
while not clicked:
	for event in pygame.event.get():
		tupleXY = (0, 0)
		if event.type == pygame.MOUSEBUTTONUP:
			tupleXY = pygame.mouse.get_pos()
			x = tupleXY[0]
			y = tupleXY[1]
			if x >= 150 and x <= 650:
				if y >= 450 and y <= 650:
					clicked = True
			if x >= 275 and x <= 525:
				if y >= 650 and y <= 750:
					clicked = True
		if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q] != 0:
			clicked = True
