import colorsText
import math
import vector
import circle
import sys
import copy
import time
import console

class Screen(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.display = [[' ' for pixel in range(width)] for row in range(height)]

	def __str__(self):
		output = '\n' * ((console.HEIGHT - self.height)/2)
		newDisplay = copy.deepcopy(self.display)
		newDisplay.reverse()
		for row in newDisplay:
			output += ' ' * ((console.WIDTH - self.width*2)/2)
			for pixel in row:
				output += pixel + ' '
			output += ' ' * ((console.WIDTH - self.width*2)/2) + '\n'
		output += '\n' * ((console.HEIGHT - self.height)/2)
		return output

	def clear(self):
		self.display = [[' ' for pixel in range(self.width)] for row in range(self.height)]		

	def vector(self, start, angle, length, color):
		self.display = vector.vector(self.display, start, angle, length, color=color)

	def circle(self, start, radius, color):
		self.display = circle.circle(self.display, start, radius, color=color)

if console.WIDTH*.5 >= console.HEIGHT:
	width, height = console.HEIGHT*1.6, console.HEIGHT*.8
else:
	width, height = console.WIDTH*.8, console.WIDTH*.4

screen = Screen(int(width), int(height))

i = 0
while True:
	try:
		screen.clear()

		screen.circle((int(width/2), int(height/2)), int((float(height)/2)*(((float(i)%9)+1)/10)), i%9)
		screen.circle((int(width/2), int(height/2)), int((float(height)/2)*((((float(i)-4)%9)+1)/10)), (i-4)%9)

		screen.circle((int(width/4), int(height/4)), ((i+4)%3)+1, (i+1)%9)
		screen.circle((int(3*width/4), int(height/4)), ((i+3)%3)+1, (i+2)%9)
		screen.circle((int(width/4), int(3*height/4)), ((i+2)%3)+1, (i+3)%9)
		screen.circle((int(3*width/4), int(3*height/4)), ((i+1)%3)+1, (i+4)%9)

		sys.stdout.write(str(screen))
		i += 1
		time.sleep(.1)
	except KeyboardInterrupt:
		print '\n' * console.HEIGHT
		sys.exit()
