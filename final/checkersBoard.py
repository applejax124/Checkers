#!~pbui/pub/anaconda2-4.1.1/bin
#CHECKERSBOARD

import pygame
import findCell
import classes
import gameplay
import screens1
import functions

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
                    pygame.draw.circle(screen, (250, 0, 0), (x+40, y+40), 30)
                if block.type == 'rk':
                    pygame.draw.circle(screen,(250,0,0),(x+40, y+40), 30, 10)
                if block.type == 'b':
                    pygame.draw.circle(screen, (0, 0, 0), (x+40, y+40), 30)
                if block.type == 'bk': 
                    pygame.draw.circle(screen,(0, 0, 0),(x+40, y+40), 30, 10)


def playGame(multiplayer):
    pygame.init()
    screen = pygame.display.set_mode((800,800))

    play = True #continue game play until play == False

    clock = pygame.time.Clock()

    #instantiate board object and draw screen
    gameBoard = classes.board()
    boardC(screen, gameBoard)
    pieces(screen, gameBoard)
    pygame.display.flip()

    player = 0; 

    moveSelect = True 

    while (play):

        if player == 0: #player 1
            check_type = 'r'
        elif player == 1: #player 2 or AI
            check_type = 'b'

        if not multiplayer and player == 1: #single player mode
#            piece1 = 
#            piece2 = 

            #highlighting/selectpiece
            type1 = gameBoard.b[piece1].type
            type2 = gameBoard.b[piece2].type
            p = gameplay.validMove(gameBoard.b[piece1], gameBoard.b[piece2], gameBoard)
            type2 = gameBoard.b[p].type
            functions.selectpiece(piece1, gameBoard, check_type, screen)
            pygame.time.delay(500)

            #move piece
            functions.makemove(piece1, piece2, p, gameBoard)

            #update screen
            screen.fill((0,0,0))
            boardC(screen, gameBoard)
            pieces(screen, gameBoard)

            #check if there is a winner
            winner = functions.iswinner(cell2, type2, type1, gameBoard)
            if winner != 0:
                return winner

            #update player
            player = (player + 1) % 2
            continue

	for event in pygame.event.get(): #multiplayer mode

            #quit the game
            if functions.quit(event.type) == 0:
                return 0

            #highlighting/select piece
            if event.type==pygame.MOUSEBUTTONUP and moveSelect:
		(x,y) = pygame.mouse.get_pos()
		cell = findCell.checkCell(x,y) #get cell number based on mouse position
                type1 = gameBoard.b[cell].type
		if functions.selectpiece(cell, gameBoard, check_type, screen) == 0:
                    moveSelect = False
                    continue

            #move the checker
	    if event.type==pygame.MOUSEBUTTONUP and not moveSelect:
                (x,y) = pygame.mouse.get_pos()
                cell2 = findCell.checkCell(x,y) #get board square number
                p = gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard)
                type2 = gameBoard.b[p].type
                moveSelect = True
                
                #move the selected piece if the move is valid
                functions.makemove(cell, cell2, p, gameBoard)

                #update screen
                screen.fill((0,0,0))
  		boardC(screen, gameBoard)
                pieces(screen, gameBoard)
                
                #check if there is a winner
                winner = functions.iswinner(cell2, type2, type1, gameBoard)
                if winner != 0:
                    return winner

                #next player's turn
                player = (player + 1) % 2

        clock.tick(5)
	pygame.display.flip()
