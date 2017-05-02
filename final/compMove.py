#!/usr/bin/env python2.7

import gameplay
import random

#sets for adders and valid cell movements
#MAKE A DICTIONARY
VALID_CELLS = {3: [5,6,7,13,14,15,21,22,23], \
    4: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27], \
    5: [0,1,2,8,9,10,16,17,18,24,25,26], \
    7: [1,2,3,5,6,7,9,10,11,13,14,15,17,18,19,21,22,23], \
    9: [0,1,2,4,5,6,8,9,10,12,13,14,16,17,18,20,21,22], \
    -3: [8,9,10,16,17,18,24,25,26], \
    -4: [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31], \
    -5: [5,6,7,13,14,15,21,22,23,29,30,31], \
    -7: [8,9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30], \
    -9: [9,10,11,13,14,15,17,18,19,21,22,23,25,26,27,29,30,31]}

def makeMove(board):
    play = True
    while play:

        #randomly choose one of the adders
        movesize = [3, 4, 5, 7, 9, -3, -4, -5, -7, -9]
        mv = movesize[random.randrange(0,10)]

        #choose random cell in board for which mv is a valid move
        cell = VALID_CELLS[mv][random.randrange(0, len(VALID_CELLS[mv] ))]

        #set new cell
        new_cell = cell + mv

        #check piece type and valid move
        if board.b[cell].type != 'b' and board.b[cell].type != 'bk':
            continue
        else:
            if gameplay.validMove(board.b[cell], board.b[new_cell], board) != 1:
                #print "mv: ",
                #print mv,
                #print " | cell: ",
                #print cell,
                #print " | new_cell: ",
                #print new_cell
                return (cell, new_cell)
