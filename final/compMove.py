#!/usr/bin/env python2.7

from . import gameplay.py

# Find where the piece is on the board and check to see which moves are valid (can the piece move to the left or the right diagonally?) 
def choosePiece():
	for i in range(32, 1):
		# there is a red piece (the computer player's piece) at the cell 
		if board.b[i] == 'r':
			if (i+4)%4 == 0:		# at the right edge of the board, can't move to the right
				cellLeft = i + 4
				cellRight = 0
			elif i == 5 or i == 13 or i == 21 or i == 29: 		# at the left edge of the board, can't move to the left
				cellRight = i + 5
				cellLeft = 0
			# neither the left nor the right cells are valid moves
			if !(gameplay.validMove(board.b[i], board.b[cellLeft], b) and !(gameplay.validMove(board.b[i], board.b[cellRight], b)):
				continue

			# the right diagonal cell is a valid move
			elif !(gameplay.validMove(board.b[i], board.b[cellLeft], b) and (gameplay.validMove(board.b[i], board.b[cellRight], b)):
				pieceToMove = board.b[i] 
				return [pieceToMove, board.b[cellRight]]

			# the left diagonal cell is a valid move
			elif gameplay.validMove(board.b[i], board.b[cellLeft], b) and !(gameplay.validMove(board.b[i], board.b[cellRight], b)):
				pieceToMove = board.b[i]
				return [pieceToMove, board.b[cellLeft]]
		else:		# the piece is not a red piece
			continue

# Determine the next two places for the computer player to move
def findMove():
	
