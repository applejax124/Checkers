#!/usr/bin/env python2.7

import gameplay

def makeMove(board):
	for cell in board:
		if validMove(board.b[cell], newCell + 5, board):
			return (board.b[cell], newCell + 5)
		elif validMove(board.b[cell], newCell + 4, board):
			return (board.b[cell], newCell + 4)
		elif validMove(boad.b[cell], newCell + 3, board):
			return (board.b[cell], newCell + 3)
		else:
			continue 
