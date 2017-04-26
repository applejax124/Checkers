#!/usr/bin/env python

class board:
    def __init__(self):
	self.b = []
	for i in range(1,13): #(1, 13):
        	self.b.append(piece('r'))
		self.b[i-1].setCell(i)
	for i in range(13,21): #(13, 21):
		self.b.append(piece(' '))
                self.b[i-1].setCell(i)
	for i in range(21,33): #(21, 33):
		self.b.append(piece('b'))
		self.b[i-1].setCell(i)

    def movePiece(self, new_cell, old_cell):
        t = self.b[old_cell].type
	self.b[new_cell].setType(t)
	self.b[old_cell].setType(' ')

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
