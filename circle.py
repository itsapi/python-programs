import math
import colorsText

def circle(display, start, radius, char='#', color=False):
	def output():
		if (color == False):
			return char
		else:
			return colorsText.printout(char, color)

	for x in range(int(radius)):
		y = int(math.sqrt(radius*radius - x*x))
		display[int(start[1]+y)][int(start[0]+x)] = output()
		display[int(start[1]-y)][int(start[0]+x)] = output()
		display[int(start[1]+y)][int(start[0]-x)] = output()	
		display[int(start[1]-y)][int(start[0]-x)] = output()

		display[int(start[1]+x)][int(start[0]+y)] = output()
		display[int(start[1]+x)][int(start[0]-y)] = output()
		display[int(start[1]-x)][int(start[0]+y)] = output()
		display[int(start[1]-x)][int(start[0]-y)] = output()
	return display
