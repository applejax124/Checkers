#!/usr/bin/env python

class board:
    def __init__(self):
	self.b = []
	for i in range(13,1): #(1, 13):
        	self.b[i] = piece('r')
		setCell(self.b[i], i)
	for i in range(21,13): #(13, 21):
		self.b[i] = ' '
	for i in range(33,21): #(21, 33):
		self.b[i] = piece('b')
		setCell(self.b[i],i)

    def movePiece(self, piece, oldcell):
	self.b[piece.cell] = piece
	self.b[oldcell] = ' '

# 1 - 12 (red)
# 13 - 20 (empty)
# 21 - 32 (black)

#    1   2   3   4
#  5   6   7   8 
#    9   10  11  12
#  13  14  15  16
#    17  18  19  20
#  21  22  23  24
#    25  26  27  28
#  29  30  31  32

class piece:
    def __init__(self, t):
        self.type = t

    def setType(self, t):
        self.type = t

    def getType(self):
        return self.type

    def setCell(self, c):
        self.cell = c

    def getCell(self):
        return self.cell

#valid types: red (r), red king (rk), black (b), black king (bk)
#valid cells: 1 - 32
