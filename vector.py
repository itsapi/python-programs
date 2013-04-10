import math
import colorsText

def vector(display, start, angle, length, color):
	xLength = length * math.sin(math.radians(angle))
	yLength = length * math.cos(math.radians(angle))
	if (angle-45) % 180 < 90:
		if xLength <= 0:
			for xOff in range(0, int(xLength), -1):
				display[int(start[1] + ((xLength-xOff)/math.tan(math.radians(angle))))][int(start[0]+xLength-xOff)] = colorsText.printout('#', color)
		else:
			for xOff in range(int(xLength)):
				display[int(start[1] + ((xLength-xOff)/math.tan(math.radians(angle))))][int(start[0]+xLength-xOff)] = colorsText.printout('#', color)
	else:
		if yLength <= 0:
			for yOff in range(0, int(yLength), -1):
				display[int(start[1]+yLength-yOff)][int(start[0] + ((yLength-yOff)*math.tan(math.radians(angle))))] = colorsText.printout('#', color)
		else:
			for yOff in range(int(yLength)):
				display[int(start[1]+yLength-yOff)][int(start[0] + ((yLength-yOff)*math.tan(math.radians(angle))))] = colorsText.printout('#', color)
	return display
