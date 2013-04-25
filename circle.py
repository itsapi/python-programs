import math
import colorsText

def circle(display, start, radius, char='#', color=False):
	def output():
		if (color == False):
			return char
		else:
			return colorsText.printout(char, color)

	for x in range(radius):
		y = int(math.sqrt(radius*radius - x*x))
		display[start[1]+y][start[0]+x] = output()
		display[start[1]-y][start[0]+x] = output()
		display[start[1]+y][start[0]-x] = output()	
		display[start[1]-y][start[0]-x] = output()

		display[start[1]+x][start[0]+y] = output()
		display[start[1]+x][start[0]-y] = output()
		display[start[1]-x][start[0]+y] = output()
		display[start[1]-x][start[0]-y] = output()
	return display
