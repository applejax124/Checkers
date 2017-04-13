#!usr/bin/python2.7

#COUNTS PIECES
def pieceCount(ptype, board): #takes in the type of piece & the board object
    count = 0;
    for cell in board:
        if cell.type == ptype:
            count++
    return count

#CHECKS IF THERE IS A WINNER
def winner(ptype, count): #takes in the type of piece & a count
    if !count:
        return false

#CHECKS FOR VALID MOVES
def validMove(piece, player, newCell): #takes in a piece object & player number & new cell location

    movesize = getMoveSize(piece.cell, newCell) #returns the min jump size (max = movesize + 1)

    if   piece.type == 'r': #can only move UP cell numbers
        if (newCell - piece.cell == movesize || newCell - piece.cell == movesize+1) && newCell == ' ':
            return true
        else:
            return checkJump(piece, newCell)
    elif piece.type == 'b': #can only move DOWN cell numbers
        if (piece.cell - newCell == movesize || piece.cell - newCell == movesize+1) && newCell == ' ':
            return true
        else:
            return checkJump(piece, newCell)
    elif piece.type == 'bk':
        if (piece.cell - newCell == movesize || piece.cell - newCell == movesize+1) && newCell == ' ':
            return true
        elif (newCell - piece.cell == movesize || newCell - piece.cell == movesize+1) && newCell == ' ':
            return true
        else:
            return checkJump(piece, newCell)
    elif piece.type == 'rk':
        if (piece.cell - newCell == movesize || piece.cell - newCell == movesize+1) && newCell == ' ':
            return true
        elif (newCell - piece.cell == movesize || newCell - piece.cell == movesize+1) && newCell == ' ':
            return true
        else:
            return checkJump(piece, newCell)

#CHECKS A JUMP
def checkJump(piece, newCell): #returns true if valid jump


#GETS MOVE SIZE BASED ON ROW
def getMoveSize(currCell, newCell): #the amount of cells the piece can move depends on the row 
                                    #it is in & the row it wants to move to
    movesize = 0

    if   currCell >=  1 && currCell <=  4:
        return 4
    elif currCell >=  5 && currCell <=  8:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >=  9 && currCell <= 12:
        if neeCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 13 && currCell <= 16:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 17 && currCell <= 20:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 21 && currCell <= 24:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 25 && currCell <= 28:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 29 && currCell <= 32:
        return 4
