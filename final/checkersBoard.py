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
    for block in board.b:
	for key, value in findCell.cells.items():
            if value == block.cell:
                x, y = key
            if block == 'r':
                pygame.draw.circle(screen, (250, 0, 0), (x+40, y+40), 20)
            if block == 'rk':
                pygame.draw.circle(screen,(153,0,0),(x+40, y+40),20)
            if block == 'b':
                pygame.draw.circle(screen, (0, 0, 0), (x+40, y+40), 20)
            if block == 'bk': 
                pygame.draw.circle(screen,(64, 64, 64),(x+40, y+40),20)


def playGame(playernum):
    if playernum==2:
        pygame.init()
        screen = pygame.display.set_mode((800,800))
	play = True
	clock = pygame.time.Clock()

	#cell2 = 0
	gameBoard = classes.board() 
	boardC(screen, gameBoard)
	pieces(screen, gameBoard)
	pygame.display.flip()

        while (play):

	    moveSelect = True

    	    for event in pygame.event.get():

                #highlighting/select piece
                if event.type==pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] and moveSelect:
    		    (x,y) = pygame.mouse.get_pos()
    		    cell = findCell.checkCell(x,y) #get board square number w func and pygame.mouse.get_pos()
    		    if cell != 0 and board.b[cell] != ' ':
                        pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(x, y, 80, 80))
                        moveSelect = False
                        continue
    
                #move the checker
    	        if event.type==pygame.MOUSEBUTTONUP and pygame.mouse.get_pressed()[0] and not moveSelect:
                    (x,y) = pygame.mouse.get_pos()
                    cell2 = findCell.checkCell(x,y) #get board sqaure number
                    moveSelect = True
                    if gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard):
                        gameBoard.movePiece(gameBoard.b[cell2], gameBoard.b[cell])
    		    screen.fill((0,0,0))
    		    boardC(screen, gameBoard)
    		    pieces(screen, gameBoard)

                #quit the game if Q is pressed
                if event.type==pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_q] != 0:
                    #(s, y) = pygame.mouse.get_pos()
                    play = False	
    
                #check if there is a winner
#                if cell2 and gameplay.winner(gameBoard.b[cell2].type, gameplay.pieceCount(gameBoard.b[cell2].type, gameBoard)):
#                    play = False
#    		    if gameBoard.b[cell2] == 'r' or gameBoard.b[cell2] == 'rk': return 1
#                   elif gameBoard.b[cell2] == 'b' or gameBoard.b[cell2] == 'bk': return 2

            clock.tick(5)
    	    pygame.display.flip()
