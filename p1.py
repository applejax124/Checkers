#!/~pbui/pub/anaconda2-4.1.1/bin/python

import pygame

pygame.init()
screen = pygame.display.set_mod((400, 300))
done = False

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 200, 200))

	pygame.display.flip()
