#!~pbui/pub/anaconda2-4.1.1/bin

# PURPOSE: This file is used to give each physical pixel value (the top left corner of a space on the board) a number, making it easier to determine whether or not a player makes a valid move on the board. 

#create the dictionary of possible values.
cells = {}

# the x, y coordinate pairs of the top left corner for each cell
tuples = [(160, 80), (320, 80), (480, 80), (640, 80), 
		(80, 160), (240, 160), (400, 160), (560, 160), 
		(160, 240), (320, 240), (480, 240), (640, 240),
		(80, 320), (240, 320), (400, 320), (560, 320),
		(160, 400), (320, 400), (480, 400), (640, 400),
		(80, 480), (240, 480), (400, 480), (560, 480),
		(160, 560), (320, 560), (480, 560), (640, 560),
		(80, 640), (240, 640), (400, 640), (560, 640)]

# assigns a value (1 - 32, number of valid spaces on the board) to each pixel x-y pair on the board
for i in range(1, len(tuples) + 1):
	cells[i] = tuples[i-1]
	print("{} : {}" .format(i, cells[i]))
