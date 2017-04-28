#!/pbui/pub/anaconda2-4.1.1/bin

import gameplay
import networkx as nx

def getMoves():
	moves = nx.Graph()
	moves.add_edge(1, 5, weight=0)
	moves.add_edge(1, 6, weight=0)
	moves.add_edge(2, 6, weight=0)
	moves.add_edge(2, 7, weight=0)
	moves.add_edge(3, 7, weight=0)
	moves.add_edge(3, 8, weight=0)
	moves.add_edge(4, 8, weight=0)

	moves.add_edge(5, 9, weight=0)
	moves.add_edge(6, 9, weight=0)
	moves.add_edge(6, 10, weight=0)
	moves.add_edge(7, 10, weight=0)
	moves.add_edge(7, 11, weight=0)
	moves.add_edge(8, 11, weight=0)
	moves.add_edge(8, 12, weight=0)

	moves.add_edge(9, 13, weight=0)
	moves.add_edge(9, 14, weight=0)
	moves.add_edge(10, 14, weight=0)
	moves.add_edge(10, 15, weight=0)
	moves.add_edge(11, 15, weight=0)
	moves.add_edge(11, 16, weight=0)
	moves.add_edge(12, 16, weight=0)

	moves.add_edge(13, 17, weight=0)
	moves.add_edge(14, 17, weight=0)
	moves.add_edge(14, 18, weight=0)
	moves.add_edge(15, 18, weight=0)
	moves.add_edge(15, 19, weight=0)
	moves.add_edge(16, 19, weight=0)
	moves.add_edge(16, 20, weight=0)

	moves.add_edge(17, 21, weight=0)
	moves.add_edge(17, 22, weight=0)
	moves.add_edge(18, 22, weight=0)
	moves.add_edge(18, 23, weight=0)
	moves.add_edge(19, 23, weight=0)
	moves.add_edge(19, 24, weight=0)
	moves.add_edge(20, 24, weight=0)

	moves.add_edge(21, 25, weight=0)
	moves.add_edge(22, 25, weight=0)
	moves.add_edge(22, 26, weight=0)
	moves.add_edge(23, 26, weight=0)
	moves.add_edge(23, 27, weight=0)
	moves.add_edge(24, 27, weight=0)
	moves.add_edge(24, 28, weight=0)

	moves.add_edge(25, 29, weight=0)
	moves.add_edge(25, 30, weight=0)
	moves.add_edge(26, 30, weight=0)
	moves.add_edge(26, 31, weight=0)
	moves.add_edge(27, 31, weight=0)
	moves.add_edge(27, 32, weight=0)
	moves.add_edge(28, 32, weight=0)
	return moves


def getMovesKing():
	moves = nx.Graph()
	moves.add_edge(1, 5, weight=0)
	moves.add_edge(1, 6, weight=0)
	moves.add_edge(2, 6, weight=0)
	moves.add_edge(2, 7, weight=0)
	moves.add_edge(3, 7, weight=0)
	moves.add_edge(3, 8, weight=0)
	moves.add_edge(4, 8, weight=0)

	moves.add_edge(5, 9, weight=0)
	moves.add_edge(5, 1, weight=0)
	moves.add_edge(6, 9, weight=0)
	moves.add_edge(6, 10, weight=0)
	moves.add_edge(6, 1, weight=0)
	moves.add_edge(6, 2, weight=0)
	moves.add_edge(7, 10, weight=0)
	moves.add_edge(7, 11, weight=0)
	moves.add_edge(7, 2, weight=0)
	moves.add_edge(7, 3, weight=0)
	moves.add_edge(8, 11, weight=0)
	moves.add_edge(8, 12, weight=0)
	moves.add_edge(8, 3, weight=0)
	moves.add_edge(8, 4, weight=0)

	moves.add_edge(9, 13, weight=0)
	moves.add_edge(9, 14, weight=0)
	moves.add_edge(9, 5, weight=0)
	moves.add_edge(9, 6, weight=0)
	moves.add_edge(10, 14, weight=0)
	moves.add_edge(10, 15, weight=0)
	moves.add_edge(10, 6, weight=0)
	moves.add_edge(10, 7, weight=0)
	moves.add_edge(11, 15, weight=0)
	moves.add_edge(11, 16, weight=0)
	moves.add_edge(11, 7, weight=0)
	moves.add_edge(11, 8, weight=0)
	moves.add_edge(12, 16, weight=0)
	moves.add_edge(12, 8, weight=0)

	moves.add_edge(13, 17, weight=0)
	moves.add_edge(13, 9, weight=0)
	moves.add_edge(14, 9, weight=0)
	moves.add_edge(14, 10, weight=0)
	moves.add_edge(15, 10, weight=0)
	moves.add_edge(15, 11, weight=0)
	moves.add_edge(16, 11, weight=0)
	moves.add_edge(16, 12, weight=0)
	moves.add_edge(14, 17, weight=0)
	moves.add_edge(14, 18, weight=0)
	moves.add_edge(15, 18, weight=0)
	moves.add_edge(15, 19, weight=0)
	moves.add_edge(16, 19, weight=0)
	moves.add_edge(16, 20, weight=0)

	moves.add_edge(17, 21, weight=0)
	moves.add_edge(17, 22, weight=0)
	moves.add_edge(18, 22, weight=0)
	moves.add_edge(18, 23, weight=0)
	moves.add_edge(19, 23, weight=0)
	moves.add_edge(19, 24, weight=0)
	moves.add_edge(20, 24, weight=0)
	moves.add_edge(17, 13, weight=0)
	moves.add_edge(17, 14, weight=0)
	moves.add_edge(18, 14, weight=0)
	moves.add_edge(18, 15, weight=0)
	moves.add_edge(19, 15, weight=0)
	moves.add_edge(19, 16, weight=0)
	moves.add_edge(20, 16, weight=0)

	moves.add_edge(21, 25, weight=0)
	moves.add_edge(22, 25, weight=0)
	moves.add_edge(22, 26, weight=0)
	moves.add_edge(23, 26, weight=0)
	moves.add_edge(23, 27, weight=0)
	moves.add_edge(24, 27, weight=0)
	moves.add_edge(24, 28, weight=0)
	moves.add_edge(21, 17, weight=0)
	moves.add_edge(22, 17, weight=0)
	moves.add_edge(22, 18, weight=0)
	moves.add_edge(23, 18, weight=0)
	moves.add_edge(23, 19, weight=0)
	moves.add_edge(24, 19, weight=0)
	moves.add_edge(24, 20, weight=0)

	moves.add_edge(25, 29, weight=0)
	moves.add_edge(25, 30, weight=0)
	moves.add_edge(26, 30, weight=0)
	moves.add_edge(26, 31, weight=0)
	moves.add_edge(27, 31, weight=0)
	moves.add_edge(27, 32, weight=0)
	moves.add_edge(28, 32, weight=0)
	moves.add_edge(25, 21, weight=0)
	moves.add_edge(25, 22, weight=0)
	moves.add_edge(26, 22, weight=0)
	moves.add_edge(26, 23, weight=0)
	moves.add_edge(27, 23, weight=0)
	moves.add_edge(27, 24, weight=0)
	moves.add_edge(28, 24, weight=0)

	moves.add_edge(29, 25, weight=0)
	moves.add_edge(30, 25, weight=0)
	moves.add_edge(30, 26, weight=0)
	moves.add_edge(31, 26, weight=0)
	moves.add_edge(31, 27, weight=0)
	moves.add_edge(32, 27, weight=0)
	moves.add_edge(32, 28, weight=0)
	return moves

def checkNextMove(moves):
	for (currloc, newloc, w) in moves:
		if validMove

def checkBlackPiece(moves):
	for (currloc, newloc, w) in moves:
		if board.b[newloc] == 'b':
			if checkNextMove():
				moves[currloc][newloc]['weight']+=5 

def mainfunc():
	moves = {}
	for i in xrange(32, 1):
		if board.b[i] == 'r':
			moves = getMoves()
		elif board.b[i] == 'rk':
			moves = getMovesKing()

