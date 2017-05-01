#!~pbui/pub/anaconda2-4.1.1/bin
#CHECKERSBOARD

import pygame
import findCell
import classes
import gameplay
import screens1

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

    play = True

    clock = pygame.time.Clock()

    gameBoard = classes.board()
    boardC(screen, gameBoard)
    pieces(screen, gameBoard)
    pygame.display.flip()

    player = 0; 

    moveSelect = True

    while (play):

        if player == 0:
            check_type = 'r'
        elif player == 1:
            check_type = 'b'

        if not multiplayer && player == 1: #single player mode
            player = (player + 1) % 2
            continue

	for event in pygame.event.get(): #multiplayer mode

            #quit the game
            if event.type==pygame.MOUSEBUTTONUP:
                (s, y) = pygame.mouse.get_pos()
                if s >= 730 and s <= 780 and y >= 740 and y <= 760:
                    return 0

            #highlighting/select piece
            if event.type==pygame.MOUSEBUTTONUP and moveSelect:
		(x,y) = pygame.mouse.get_pos()
		cell = findCell.checkCell(x,y) #get board square number w func and pygame.mouse.get_pos()
                type1 = gameBoard.b[cell].type
		if cell >= 0 and gameBoard.b[cell].type != ' ' and type1 == check_type or type1 == check_type + 'k':
                    (s,r) = findCell.getPos(cell)
                    pygame.draw.rect(screen, (0, 0, 192), pygame.Rect(s, r, 80, 80), 4)
                    moveSelect = False
                    continue

            #move the checker
	    if event.type==pygame.MOUSEBUTTONUP and not moveSelect:
                (x,y) = pygame.mouse.get_pos()
                cell2 = findCell.checkCell(x,y) #get board square number
                moveSelect = True
                p = gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard)
                type2 = gameBoard.b[p].type
                if cell2 >= 0 and p == 0:
                    #movePiece
                    t = gameBoard.b[cell2].getType()
                    gameBoard.b[cell2].setType(gameBoard.b[cell].getType()) 
                    gameBoard.b[cell].setType(t)
                elif cell2 >= 0 and p > 1:
                    #jumpPiece
                    t = gameBoard.b[cell2].getType()
                    gameBoard.b[cell2].setType(gameBoard.b[cell].getType()) 
                    gameBoard.b[cell].setType(t)
                    gameBoard.b[p].setType(' ')
                #make kings
                if type1 == 'b' and gameBoard.b[cell2].cell <= 3 and gameBoard.b[cell2].cell >= 0:
                    gameBoard.b[cell2].setType('bk')
                if type1 == 'r' and gameBoard.b[cell2].cell <= 31 and gameBoard.b[cell2].cell >= 28:
                    gameBoard.b[cell2].setType('rk')
                #update screen
                screen.fill((0,0,0))
  		boardC(screen, gameBoard)
                pieces(screen, gameBoard)
                
                #check if there is a winner
                if cell2 and gameplay.pieceCount(type2, gameBoard) == 0:
                    if type1 == 'r' or type1 == 'rk': return 1
                    elif type1 == 'b' or type1 == 'bk': return 2

                #next player's turn
                player = (player + 1) % 2

        clock.tick(5)
	pygame.display.flip()
