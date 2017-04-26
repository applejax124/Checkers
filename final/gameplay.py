#!usr/bin/python2.7

#COUNTS PIECES
def pieceCount(ptype, board): #takes in the type of piece & the board object
    count = 0;
    for cell in board.b:
        if cell.type == ptype:
            count = count + 1
    return count

#CHECKS IF THERE IS A WINNER
def winner(ptype, count): #takes in the type of piece & a count
    if count == 0:
        return False

#CHECKS FOR VALID MOVES
def validMove(piece, newCell, board): #takes in a piece object & new cell location

    movesize = getMoveSize(piece.cell, newCell.cell) #returns the min jump size (max = movesize + 1)

    if   piece.type == 'r': #can only move UP cell numbers
        if (newCell.cell - piece.cell == movesize or newCell.cell - piece.cell == movesize+1) and newCell.type == ' ':
            return True
        elif (newCell.cell - piece.cell == 7 or newCell.cell - piece.cell == 9):
            return checkJump(piece, newCell, board)
        else:
            return False

    elif piece.type == 'b': #can only move DOWN cell numbers
        if (piece.cell - newCell.cell == movesize or piece.cell - newCell.cell == movesize+1) and newCell.type == ' ':
            return True
        elif (newCell.cell - piece.cell == -7 or newCell.cell - piece.cell == -9):
            return checkJump(piece, newCell, board)
        else:
            return False

    elif piece.type == 'bk':
        if (piece.cell - newCell.cell == movesize or piece.cell - newCell.cell == movesize+1) and newCell.type == ' ':
            return True
        elif (newCell.cell - piece.cell == movesize or newCell.ccell - piece.cell == movesize+1) and newCell.type == ' ':
            return True
        elif (newCell.cell - piece.cell == 7 or newCell.cell - piece.cell == 9 or newCell.cell - piece.cell == -7 or newCell.cell - piece.cell == -9):
            return checkJump(piece, newCell, board)
        else:
            return False

    elif piece.type == 'rk':
        if (piece.cell - newCell.cell == movesize or piece.cell - newCell.cell == movesize+1) and newCell.type == ' ':
            return True
        elif (newCell.cell - piece.cell == movesize or newCell.cell - piece.cell == movesize+1) and newCell.cell == ' ':
            return True
        elif (newCell.cell - piece.cell == 7 or newCell.cell - piece.cell == 9 or newCell.cell - piece.cell == -7 or newCell.cell - piece.cell == -9):
            return checkJump(piece, newCell, board)
        else:
            return False

#CHECKS A JUMP
def checkJump(piece, newCell, board): #returns true if valid jump

    midCell = piece.cell + getMoveSize(piece.cell, newCell.cell)

    if board[midCell].type != piece.type and board[midCell].type != piece.type + 'k' and board[midCell].type != ' ':
        return True
    else:
        return False


#GETS MOVE SIZE BASED ON ROW
def getMoveSize(currCell, newCell): #the amount of cells the piece can move depends on the row 
                                    #it is in & the row it wants to move to

    if   currCell >=  1 and currCell <=  4:
        return 4
    elif currCell >=  5 and currCell <=  8:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >=  9 and currCell <= 12:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 13 and currCell <= 16:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 17 and currCell <= 20:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 21 and currCell <= 24:
        if newCell < currCell:
            return 4
        else:
            return 3
    elif currCell >= 25 and currCell <= 28:
        if newCell < currCell:
            return 3
        else:
            return 4
    elif currCell >= 29 and currCell <= 32:
        return 4
    else:
        return 0
