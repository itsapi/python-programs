
import math
import curses
import time

TICK = .1
GRAVITY = 10*TICK
AIR = .1

class Particle(object):
	def __init__(self, x=0, y=0, v=0, d=0, char='@'):
		self.x = x
		self.y = y
		self.v = v
		self.d = d
		self.char = char

	def move(self, x=0, y=0):
		self.x += x
		self.y += y

	def set(self, x=0, y=0):
		self.x = x
		self.y = y

	def update(self):
		if self.v > 0:
			self.v -= AIR
		elif self.v < 0:
			self.v += AIR

		s = self.v*TICK
		self.x += s*math.sin(math.radians(self.d))
		self.y += s*math.cos(math.radians(self.d))
		self.y += abs(self.y * GRAVITY*TICK)

	def output(self, stdscr):
		stdscr.addstr(int(round(self.y)), int(round(self.x)), self.char)

def main(stdscr):
	stdscr.nodelay(1)
	man = Particle(x=10, y=10, v=20, d=100)
	while True:
		stdscr.clear()
		man.update()
		stdscr.addstr(5, 5, str((man.x, man.y)))
		man.output(stdscr)
		stdscr.refresh()
		time.sleep(TICK)

if __name__ == '__main__':
	curses.wrapper(main)
