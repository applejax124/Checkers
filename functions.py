#!/usr/bin/env python2.7
#FUNCTIONS

import pygame
import gameplay
import findCell

#Quit button on the board screen
def quit(event_type):
    if event_type == pygame.MOUSEBUTTONUP:
        (s, y) = pygame.mouse.get_pos()
        if s >= 730 and s <= 780 and y >= 740 and y <= 760:
            return 0
    return 1

#Selecting and highlighting pieces during gameplay
def selectpiece(cell, gameBoard, check_type, screen):   
    type1 = gameBoard.b[cell].getType()
    if cell >= 0 and type1 != ' ' and type1 == check_type or type1 == check_type + 'k':
        (s,r) = findCell.getPos(cell)
        if s > 0 and r > 0:
            pygame.draw.rect(screen, (0, 0, 192), pygame.Rect(s, r, 80, 80), 4)
            return 0
    return 1

def makemove(cell, cell2, p, gameBoard):
    p = gameplay.validMove(gameBoard.b[cell], gameBoard.b[cell2], gameBoard)
    type1 = gameBoard.b[cell].getType()
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

def iswinner(cell2, type2, type1, gameBoard):
    if cell2 != -1 and gameplay.pieceCount(type2, gameBoard) == 0:
        if type1 == 'r' or type1 == 'rk': 
            return 1
        elif type1 == 'b' or type1 == 'bk': 
            return 2
    else: return 0
