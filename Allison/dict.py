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

<<<<<<< HEAD
# assigns a value (1 - 32, number of valid spaces on the board) to each pixel x-y pair on the board
for i in range(1, len(tuples) + 1):
	cells[i] = tuples[i-1]
	print("{} : {}" .format(i, cells[i]))
=======
#for i in range(1, len(tuples) + 1):
#	cells[i] = tuples[i-1]
#	print("{} : {}" .format(i, cells[i]))


#Kendyll modified this so that the tuple was the key and the square was the value
count = 1
for tuple in tuples:
	cells[tuple] = count
	count = count + 1


def checkCell(mouseX, mouseY):
	xRows = [key for key in cells.keys() if key[0] <= mouseX and mouseX <= key[0]+xHeight]

	for t in xRows:
		if t[1] <= mouseY and mouseY <= t[1]+yHeight:
			return cells.get(t)

	return 0

#testing the function
print(checkCell(0, 0))
print(checkCell(200, 100))
print(checkCell(200, 250))


>>>>>>> 4e13734d8163e634f0ab0701ece5a77808b9b5ed
