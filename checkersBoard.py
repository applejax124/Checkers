#!~pbui/pub/anaconda2-4.1.1/bin

import pygame

#dictionary with board # and coordinates
#function to take mouse click and return board number

#highlight yellow when clicked
#show clicked piece and future move
#send move coordinate info to game play

def board(square):
   #quit button
   pygame.draw.rect(screen,(255,255,255),pygame.Rect(730,740,50,20))
   font = pygame.font.Font(None, 24)
   text = font.render("Quit",True,(0,0,0))
   screen.blit(text, (737,743))

   #board of squares
   #get coordinates of square
   colorAlt = 0
   for x in range (80,720,80): 
      colorAlt+=1
      for y in range (80,720,80):
	 if x is squareX and y is squareY:
	    pygame.draw.rect(screen,(255,255,0),pygame.Rect(x,y,80,80))
	    colorAlt+=1
	 else:
	    if (colorAlt % 2 == 0): color = (255,0,0)
	    else: color = (0,0,255)
            pygame.draw.rect(screen,color,pygame.Rect(x,y,80,80))
	    colorAlt+=1

def pieces(square):
   for i in range(32):
      if (): #piece is filled
	 if (i+1) is square:
	    pygame.draw.circle(screen,(255,255,0),cells[i],20)
	 else:
            pygame.draw.circle(screen,(255,255,255),cells[i],20)

pygame.init()
screen = pygame.display.set_mode((800,800))
play = True
clock = pygame.time.Clock()

board(33)
pieces(33)

while (play):
   for event in pygame.event.get():
      if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
         #get board square number w func and pygame.mouse.get_pos()
	 screen.fill((0,0,0))
	 board(33)
	 pieces(#board square number)
	 if #square is between 1 and 32
	    moveSelect = False
	    while (!moveSelect):
	       if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
		  #get board sqaure number
	          moveSelect = True
	    screen.fil((0,0,0))
	    board(#board number)
	    pieces(#previous number)
 	    #send board number to game play
	    #if move is valid change piece position in dictionary 
	    screen.fill((0,0,0))
	    board(33)
	    pieces(33)
	
      (x,y) = pygame.mouse.get_pos()
      if x >= 730 and x <= 780 and y >= 740 and y <= 760:
         play = False

      #clock.tick(60)
      pygame.display.flip()

