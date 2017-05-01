#!~pbui/pub/anaconda2-4.1.1/bin

# PURPOSE: This file is used to give each physical pixel value (the top left corner of a space on the board) a number, making it easier to determine whether or not a player makes a valid move on the board. 

#create the dictionary of possible values.
#cells =        {(160, 80) : 1, (320, 80) : 2, (480, 80) : 3, (640, 80) : 4, 
#		(80, 160) : 5, (240, 160) : 6, (400, 160) : 7, (560, 160) : 8, 
#		(160, 240) : 9, (320, 240) : 10, (480, 240) : 11, (640, 240) : 12,
#		(80, 320) : 13, (240, 320) : 14, (400, 320) : 15, (560, 320) : 16,
#		(160, 400) : 17, (320, 400) : 18, (480, 400) : 19, (640, 400) : 20,
#		(80, 480) : 21, (240, 480) : 22, (400, 480) : 23, (560, 480) : 24,
#		(160, 560) : 25, (320, 560) : 26, (480, 560) : 27, (640, 560) : 28,
#		(80, 640) : 29, (240, 640) : 30, (400, 640) : 31, (560, 640) : 32}

cells =        {(160, 80) : 0, (320, 80) : 1, (480, 80) : 2, (640, 80) : 3, 
		(80, 160) : 4, (240, 160) : 5, (400, 160) : 6, (560, 160) : 7, 
		(160, 240) : 8, (320, 240) : 9, (480, 240) : 10, (640, 240) : 11,
		(80, 320) : 12, (240, 320) : 13, (400, 320) : 14, (560, 320) : 15,
		(160, 400) : 16, (320, 400) : 17, (480, 400) : 18, (640, 400) : 19,
		(80, 480) : 20, (240, 480) : 21, (400, 480) : 22, (560, 480) : 23,
		(160, 560) : 24, (320, 560) : 25, (480, 560) : 26, (640, 560) : 27,
		(80, 640) : 28, (240, 640) : 29, (400, 640) : 30, (560, 640) : 31}


def checkCell(mouseX, mouseY):
	xRows = [key for key in cells.keys() if key[0] <= mouseX and mouseX <= key[0]+80]
	for t in xRows:
		if t[1] <= mouseY and mouseY <= t[1]+80:
			return cells.get(t)
        return -1

def getPos(cell):
    for k, c in cells.items():
        if c == cell:
            return k
