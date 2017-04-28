#!~pbui/pub/anaconda2-4.1.1/bin

import pygame
import findCell
import classes
import gameplay
import screens1
import compMove

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
                if block.type == 'r':
                    pygame.draw.circle(screen, (250, 0, 0), (x+40, y+40), 20)
                if block.type == 'rk':
                    pygame.draw.circle(screen,(153,0,0),(x+40, y+40),20)
                if block.type == 'b':
                    pygame.draw.circle(screen, (0, 0, 0), (x+40, y+40), 20)
                if block.type == 'bk': 
                    pygame.draw.circle(screen,(64, 64, 64),(x+40, y+40),20)


def playGame(playernum):
    #if playernum==2:
        pygame.init()
        screen = pygame.display.set_mode((800,800))
	play = True
	clock = pygame.time.Clock()

	#cell2 = 0
	gameBoard = classes.board()
        boardC(screen, gameBoard)
	pieces(screen, gameBoard)
	pygame.display.flip()

        moveSelect = True
	playerCurr = True
        while (play):

    	    for event in pygame.event.get():
                #quit the game
                if event.type==pygame.MOUSEBUTTONUP:
                    (s, y) = pygame.mouse.get_pos()
                    if s >= 730 and s <= 780 and y >= 740 and y <= 760:
                        play = False
                        continue

                #highlighting/select piece
                if playerCurr and event.type==pygame.MOUSEBUTTONUP and moveSelect:
    		    (x,y) = pygame.mouse.get_pos()
    		    cell = findCell.checkCell(x,y) #get board square number w func and pygame.mouse.get_pos()
    		    if cell != 0 and gameBoard.b[cell].type != ' ':
                        (s,r) = findCell.getPos(cell)
                        pygame.draw.rect(screen, (0, 0, 192), pygame.Rect(s, r, 80, 80), 4)
                        moveSelect = False
                        continue
    
                #move the checker
    	        if playerCurr and event.type==pygame.MOUSEBUTTONUP and not moveSelect:
                    (x,y) = pygame.mouse.get_pos()
                    cell2 = findCell.checkCell(x,y) #get board sqaure number
                    moveSelect = True

		    if playernum==1: playerCurr = False

                    if cell2 != 0 and gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard):
                        gameBoard.movePiece(cell2-1, cell-1)
    		    screen.fill((0,0,0))
    		    boardC(screen, gameBoard)
    		    pieces(screen, gameBoard)

		if not playerCurr:
                    old, new = compMove()
		    gameBoard.movePiece(new-1, old-1)
		    screen.fill((0,0,0))
                    boardC(screen, gameBoard)
                    pieces(screen, gameBoard)
                    playerCurr = True

                    
                #check if there is a winner
#                if cell2 and gameplay.winner(gameBoard.b[cell2].type, gameplay.pieceCount(gameBoard.b[cell2].type, gameBoard)):
#                    play = False
#    		    if gameBoard.b[cell2] == 'r' or gameBoard.b[cell2] == 'rk': return 1
#                   elif gameBoard.b[cell2] == 'b' or gameBoard.b[cell2] == 'bk': return 2

            clock.tick(5)
    	    pygame.display.flip()
