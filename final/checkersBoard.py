#!~pbui/pub/anaconda2-4.1.1/bin

import pygame
import findCell
import classes
import gameplay

def boardC(screen, board):
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

def pieces(screen, board):
   for i in range(1,33):
      if board.b[i] != ' ': #piece is filled
	 for key, value in findCell.cells.items():
	    if value is i:
	       x, y = key
         if board.b[i] == 'r' or board.b[i] == 'rk': pygame.draw.circle(screen,(255,0,0),(x+40, y+40),20)
         if board.b[i] == 'b' or board.b[i] == 'bk': pygame.draw.circle(screen,(0,0,0),(x+40, y+40),20)
         if board.b[i] == 'rk' or board.b[i] == 'bk': 
            font = pygame.font.Font(None, 24)
            text = font.render("K",True,(0,0,0))
            screen.blit(text, (x+50, y+50))
      else: print "hey"

def playGame(playernum):
   if playernum==2:
      pygame.init()
      screen = pygame.display.set_mode((800,800))
      play = True
      clock = pygame.time.Clock()

      cell2 = 0
      gameBoard = classes.board() 
      boardC(screen, gameBoard)
      #pieces(screen, gameBoard)

      while (play):
         for event in pygame.event.get():
            if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
	       (x,y) = pygame.mouse.get_pos()
               cell = findCell.checkCell(x,y) #get board square number w func and pygame.mouse.get_pos()
	       if cell >= 1 and cell <= 32 and board.b[cell] != ' ':
	          pygame.draw.circle(screen,(255,255,0),(x+40, y+40),20)
	          moveSelect = False
	          while not moveSelect:
	             if event.type==pygame.KEYDOWN and pygame.mouse.get_pressed()[0]:
		        (x,y) = pygame.mouse.get_pos()
		        cell2 = findCell.checkCell(x,y)#get board sqaure number
	                moveSelect = True
	          pygame.draw.rect(screen,(255,255,0),pygame.Rect(x,y,80,80))
		  if gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard):
		     gameBoard.movePiece(gameBoard.b[cell2], gameBoard.b[cell])	    
	          screen.fill((0,0,0))
	          boardC(screen, gameBoard)
	          pieces(screen, gameBoard)
	
            (x,y) = pygame.mouse.get_pos()
            if x >= 730 and x <= 780 and y >= 740 and y <= 760:
               play = False
	       return 0
            if cell2 and gameplay.winner(gameBoard.b[cell2].type, pieceCount(gameBoard.b[cell2].type, gameBoard)):
	       play = False
	       if gameBoard.b[cell2] == 'r' or gameBoard.b[cell2] == 'rk': return 1
	       elif gameBoard.b[cell2] == 'b' or gameBoard.b[cell2] == 'bk': return 2

            clock.tick(5)
            pygame.display.flip()

#playGame(2)
