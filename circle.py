import math
import colorsText

def circle(display, start, radius, color):
	for x in range(radius):
		y = int(math.sqrt(radius*radius - x*x))
		display[start[1]+y][start[0]+x] = colorsText.printout('#', color)
		display[start[1]-y][start[0]+x] = colorsText.printout('#', color)
		display[start[1]+y][start[0]-x] = colorsText.printout('#', color)		
		display[start[1]-y][start[0]-x] = colorsText.printout('#', color)

		display[start[1]+x][start[0]+y] = colorsText.printout('#', color)
		display[start[1]+x][start[0]-y] = colorsText.printout('#', color)
		display[start[1]-x][start[0]+y] = colorsText.printout('#', color)
		display[start[1]-x][start[0]-y] = colorsText.printout('#', color)
	return display
