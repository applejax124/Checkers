#!~pbui/pub/anaconda2-4.1.1/bin

#define cells dictionary here
cells = {}
#...

def checkCell(mouseX, mouseY):
	#list of keys that match the X-coords
	xRows = [key for key in cells.keys() if key[0] <= mouseX and mouseX <= key[0]+80]
	
	for x in xRows:
		if x[1] <= mouseY and mouseY <= x[1]+80:
			return cells.get(x)

	return 0
