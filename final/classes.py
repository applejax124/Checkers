#!/usr/bin/python2.7

class board:
    def __init__(self):
        b = []
        for i in 1 2 3 4 5 6 7 8 9 10 11 12:
            b[i] = piece('r')
            setCell(b[i],i)
        for i in 13 14 15 16 17 18 19 20:
            b[i] = ' '
        for i in 21 22 23 24 25 26 27 28 29 30 31 32:
            b[i] = piece('b')
            setCell(b[i],i)

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

    def getType(self):
        return self.type

    def setCell(self, c):
        self.cell = c

    def getCell(self):
        return self.cell

#valid types: red (r), red king (rk), black (b), black king (bk)
#valid cells: 1 - 32
