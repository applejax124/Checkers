#!usr/bin/python2.7

def pieceCount(ptype, board):
    count = 0;
    for cell in board:
        if cell.type == ptype:
            count++
    return count

def winner(ptype, count):
    if !count:
        return false

def validMove(piece, 
