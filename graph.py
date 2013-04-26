#coding=utf-8

import math
import time
import console
import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = list(range(8))

def colorText(text, color):
	return '\x1b[1;%dm' % (30+color) + str(text) + '\x1b[0m'

class Graph(object):
	def __init__(self, width, height, xScale, yScale):
		self.screen = Screen(width+1, height+1, ' ')
		self.screen.putVector(2, 0, 0, height-1, '|')
		self.screen.putVector(0, 2, 90, width-1, '-')
		self.screen.putPixel(2, 2, WHITE, '+')

		self.xSpacing = width / xScale[1]-xScale[0]
		i = 0
		for number in range(xScale[0], xScale[1]):
			self.screen.putPixel(self.xSpacing*i+2, 1, WHITE, str(number))
			if number >= 10:
				self.screen.putPixel(self.xSpacing*i+3, 1, WHITE, str(number)[1:])
			i += 1

		self.ySpacing = height / yScale[1]-yScale[0]
		i = 0
		for number in range(yScale[0], yScale[1]):
			self.screen.putPixel(0, self.ySpacing*i+2, WHITE, str(number))
			if number >= 10:
				self.screen.putPixel(1, self.ySpacing*i+2, WHITE, str(number)[1:])
			i += 1

	def data(self, yValues, color):
		i = 0
		for yValue in yValues:
			self.screen.putPixel(i*self.xSpacing+2, yValue*self.ySpacing+2, color)
			i += 1

	def draw(self):
		self.screen.output()

class Screen(object):
	def __init__(self, x, y, color):
		self.screen = [[color for i in range(x)] for j in range(y)]

	def putPixel(self, x, y, color, text='#'):
		self.screen[int(y)][int(x)] = colorText(text[:1], color)

	def putVector(self, x, y, angle, length, color):
		xLength = length * math.sin(math.radians(angle))
		yLength = length * math.cos(math.radians(angle))
		if (angle-45) % 180 < 90:
			if xLength <= 0:
				for xOff in range(0, int(xLength), -1):
					self.screen[int(y + ((xLength-xOff)/math.tan(math.radians(angle))))][int(x+xLength-xOff)] = color[:1]
			else:
				for xOff in range(int(xLength)):
					self.screen[int(y + ((xLength-xOff)/math.tan(math.radians(angle))))][int(x+xLength-xOff)] = color[:1]
		else:
			if yLength <= 0:
				for yOff in range(0, int(yLength), -1):
					self.screen[int(y+yLength-yOff)][int(x + ((yLength-yOff)*math.tan(math.radians(angle))))] = color[:1]
			else:
				for yOff in range(int(yLength)):
					self.screen[int(y+yLength-yOff)][int(x + ((yLength-yOff)*math.tan(math.radians(angle))))] = color[:1]

	def output(self):
		backwards = self.screen.reverse()
		final = ''#'\n'*(console.HEIGHT-len(self.screen))
		for row in self.screen:
			for pixel in row:
				final += pixel + ' '
			final += '\n'
		sys.stdout.write(final)

graph = Graph(31, 20, (0, 15), (0, 10))

yValues = []
for i in range(15):
	yValues.append(int(5*(math.sin(float(i))/2+1)))
	if yValues[len(yValues)-1] > 9:
		yValues[len(yValues)-1] = 9
	if yValues[len(yValues)-1] < 0:
		yValues[len(yValues)-1] = 0
graph.data(yValues, GREEN)

yValues = []
for i in range(15):
	yValues.append(int(5*(math.cos(float(i))/2+1)))
	if yValues[len(yValues)-1] > 9:
		yValues[len(yValues)-1] = 9
	if yValues[len(yValues)-1] < 0:
		yValues[len(yValues)-1] = 0
graph.data(yValues, MAGENTA)

graph.draw()
