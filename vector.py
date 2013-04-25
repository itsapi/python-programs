import math
import colorsText

def vector(display, start, angle, length, char='#', color=False):
	def output():
		if (color == False):
			return char
		else:
			return colorsText.printout(char, color)

	xLength = length * math.sin(math.radians(angle))
	yLength = length * math.cos(math.radians(angle))
	if (angle-45) % 180 < 90:
		if xLength <= 0:
			for xOff in range(0, int(xLength), -1):
				display[int(start[1] + ((xLength-xOff)/math.tan(math.radians(angle))))][int(start[0]+xLength-xOff)] = output()
		else:
			for xOff in range(int(xLength)):
				display[int(start[1] + ((xLength-xOff)/math.tan(math.radians(angle))))][int(start[0]+xLength-xOff)] = output()
	else:
		if yLength <= 0:
			for yOff in range(0, int(yLength), -1):
				display[int(start[1]+yLength-yOff)][int(start[0] + ((yLength-yOff)*math.tan(math.radians(angle))))] = output()
		else:
			for yOff in range(int(yLength)):
				display[int(start[1]+yLength-yOff)][int(start[0] + ((yLength-yOff)*math.tan(math.radians(angle))))] = output()
	return display
