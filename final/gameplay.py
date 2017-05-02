#!usr/bin/python2.7
#GAMEPLAY

#TRUE = 0
#FALSE = 1

#COUNTS PIECES
def pieceCount(ptype, board): #takes in the type of piece & the board object
    count = 0;
    for cell in board.b:
        if cell.type == ptype or cell.type == ptype + 'k':
            count = count + 1
    return count 

#CHECKS FOR VALID MOVES
def validMove(piece, newCell, board): #takes in a piece object & new cell location

    movesize = getMoveSize(piece.cell, newCell.cell) #returns the min jump size (max = movesize + 1)
    pn = piece.cell - newCell.cell
    np = newCell.cell - piece.cell

    if piece.cell == newCell.cell:
        return 1 

    if   piece.type == 'r': #can only move UP cell numbers
        if (np == movesize or np == movesize+1) and newCell.type == ' ':
            return 0
        elif (np == 7 or np == 9):
            return checkJump(piece, newCell, board, movesize, np)
        else:
            return 1

    elif piece.type == 'b': #can only move DOWN cell numbers
        if (pn == movesize or pn == movesize+1) and newCell.type == ' ':
            return 0
        elif (np == -7 or np == -9):
            return checkJump(piece, newCell, board, movesize, np)
        else:
            return 1

    elif piece.type == 'bk':
        if (pn == movesize or pn == movesize+1 or pn == movesize-1) and newCell.type == ' ':
            return 0
        elif (np == movesize or np == movesize+1 or np == movesize-1) and newCell.type == ' ':
            return 0
        elif (np == 7 or np == 9 or np == -7 or np == -9):
            return checkJump(piece, newCell, board, movesize, np)
        else:
            return 1

    elif piece.type == 'rk':
        if (pn == movesize or pn == movesize-1 or pn == movesize+1) and newCell.type == ' ':
            return 0
        elif (np == movesize or np == movesize+1 or np == movesize-1) and newCell.type == ' ':
            return 0
        elif (np == 7 or np == 9 or np == -7 or np == -9):
            return checkJump(piece, newCell, board, movesize, np)
        else:
            return 1

#CHECKS A JUMP
def checkJump(piece, newCell, board, movesize, np): #returns true if valid jump

    if np == 7:
        midCell = piece.cell + movesize
    elif np == -7:
        midCell = piece.cell - movesize
    elif np == 9:
        midCell = piece.cell + movesize + 1
    elif np == -9:
        midCell = piece.cell - movesize - 1

    #check if the move is valid based on the type of the midcell and the type of the new cell
    if board.b[midCell].type != piece.type and board.b[midCell].type != (piece.type + 'k') \
    and piece.type != board.b[midCell].type + 'k' and board.b[midCell].type != ' ' \
    and newCell.type == ' ':
        return midCell
    else:
        return 1


#GETS MOVE SIZE BASED ON ROW
def getMoveSize(currCell, newCell): #the amount of cells the piece can move depends on the  
                                    #row it's in & the row it wants to move to

    if   currCell >=  0 and currCell <=  3:
        return 4
    elif currCell >=  4 and currCell <=  7:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >=  8 and currCell <= 11:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 12 and currCell <= 15:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 16 and currCell <= 19:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 20 and currCell <= 23:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 24 and currCell <= 27:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 28 and currCell <= 31:
        return 4
    else:
        return 1
