#!/~pbui/pub/anaconda2-4.1.1/bin/python

#program opens window and displays shapes until space button clicked

import pygame

pygame.init() #initialize all pygame modules
screen = pygame.display.set_mode((400, 400)) #open 400x400 window
done = False

while not done:
	#rectangle
	pygame.draw.rect(screen,(250,0,0),pygame.Rect(10,10,50,50))
	#circle
	pygame.draw.circle(screen,(0,250,0),(100,100),50)
	#triangle
	pygame.draw.polygon(screen,(0,0,250),[(250,250),(200,300),(300,300)])
	#line
	pygame.draw.line(screen,(250,250,250),(350,350),(400,400),50)
	
        for event in pygame.event.get():
        	if event.type == pygame.KEYDOWN and event.key==pygame.K_SPACE:
		#checks if space button clicked
                	done = True
        
        pygame.display.flip() #display changes to screen



