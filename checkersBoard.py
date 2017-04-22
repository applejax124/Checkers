#!~pbui/pub/anaconda2-4.1.1/bin

import pygame

def board():
   #quit button
   pygame.draw.rect(screen,(255,255,255),pygame.Rect(730,740,50,20))
   font = pygame.font.Font(None, 24)
   text = font.render("Quit",True,(0,0,0))
   screen.blit(text, (737,743))

   #board of squares
   colorAlt = 0
   for x in range (80,720,80): 
      colorAlt+=1
      for y in range (80,720,80):
         if (colorAlt % 2 == 0): color = (255,255,255)
	 else: color = (128,128,128)
         pygame.draw.rect(screen,color,pygame.Rect(x,y,80,80))
	 colorAlt+=1

def pieces():
   for i in range(32):
      if board.b[i] != ' ': #piece is filled
	 for key, value in cells.items():
	    if value is i:
	       x, y = key
         if board.b[i] == 'r' or board.b[i] == 'rk': pygame.draw.circle(screen,(255,0,0),(x+40, y+40),20)
         if board.b[i] == 'b' or board.b[i] == 'bk': pygame.draw.circle(screen,(0,0,0),(x+40, y+40),20)
         if board.b[i] == 'rk' or board.b[i] == 'bk': 
            font = pygame.font.Font(None, 24)
            text = font.render("K",True,(0,0,0))
            screen.blit(text, (x+50, y+50))

def playGame(playernum):
   if playernum==2:
      pygame.init()
      screen = pygame.display.set_mode((800,800))
      play = True
      clock = pygame.time.Clock()

      board()
      pieces()

      while (play):
         for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
	       (x,y) = pygame.mouse.get_pos()
               cell = checkCell(x,y) #get board square number w func and pygame.mouse.get_pos()
	       if cell >= 1 and cell <= 32 and board.b[cell] != ' ':
	          pygame.draw.circle(screen,(255,255,0),(x+40, y+40),20)
	          moveSelect = False
	          while (!moveSelect):
	             if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
		        (x,y) = pygame.mouse.get_pos()
		        cell2 = checkCell(x,y)#get board sqaure number
	                moveSelect = True
	          pygame.draw.rect(screen,(255,255,0),pygame.Rect(x,y,80,80))
	    
 	          #send board number to game play
	          #if move is valid change piece position in dictionary 
	          screen.fill((0,0,0))
	          board()
	          pieces()
	
            (x,y) = pygame.mouse.get_pos()
            if x >= 730 and x <= 780 and y >= 740 and y <= 760:
               play = False
            if winner(
	       return 1 #or 2
	       play = False

            #clock.tick(60)
            pygame.display.flip()

