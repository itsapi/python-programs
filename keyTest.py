import curses
import sys
import console
import time
import math
import random

def main(stdscr):
	stdscr.nodelay(1)
	score = Score()
	snake = Snake()
	food = Food(stdscr, snake, score)
	grow = False
	while True:
		stdscr.clear()

		c = stdscr.getch()
		if c == curses.KEY_RIGHT:
			snake.turn(True)
		if c == curses.KEY_LEFT:
			snake.turn(False)

		snake.screen(stdscr)
		snake.move(grow)
		grow = food.update()
		stdscr.addstr(0, 0, 'Score: ' + str(score))

		stdscr.refresh()
		time.sleep(.1)

class Score(object):
	def __init__(self):
		self.score = 0

	def __str__(self):
		return str(self.score)

	def add(self, amount):
		self.score += amount

class Particle(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def move(self, x=0, y=0):
		self.x += x
		self.y += y

	def set(self, x=0, y=0):
		self.x = x
		self.y = y

class Snake(object):
	def __init__(self, x=10, y=10, headType='=', bodyType='@'):
		self.body = []
		for xOff in range(3):
			self.body.append(Particle(x+xOff, y))
		self.direction = 0
		self.headType = headType
		self.bodyType = bodyType

	def move(self, grow=False):
		x = self.x + int(math.sin(math.radians(self.direction*90)))
		y = self.y + int(math.cos(math.radians(self.direction*90)))
		if self.checkPos(x, y):
			self.body.insert(0, Particle(x, y))
			if not grow:
				self.body.pop(len(self.body)-1)

	def turn(self, clkW):
		if clkW:
			self.direction += 1
		else:
			self.direction -= 1
		self.direction = self.direction % 4

	def screen(self, stdscr):
		for particle in self.body:
			if particle == self.body[0]:
				char = self.headType
			else:
				char = self.bodyType

			stdscr.addstr(particle.x, particle.y, char)

	def checkPos(self, x, y):
		if 0 < x < console.WIDTH or 0 < y < console.HEIGHT:
			return True
		else:
			return False

	@property
	def x(self):
		return self.body[0].x

	@property
	def y(self):
		return self.body[0].y

class Food(Particle):
	def __init__(self, stdscr, snake, score):
		self.stdscr = stdscr
		self.snake = snake
		self.score = score
		self.new()

	def new(self):
		self.food = Particle(random.randint(5, console.WIDTH-5), random.randint(5, console.HEIGHT-5))

	def update(self):
		if self.food.y == self.snake.x and self.food.x == self.snake.y:
			self.new()
			self.score.add(1)
			grow = True
		else:
			grow = False
		self.stdscr.addstr(self.food.y, self.food.x, '#')
		return grow

curses.wrapper(main)