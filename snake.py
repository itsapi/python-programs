#WELCOME TO SNAKE

import curses
import sys
import console
import time
import math
import random
import pickle
import letters
import colorsText

TICK = .1

def init():
        return Score(), Snake()

def die(snake, score):
	def tempScr(stdscr):
		stdscr.clear()
		stdscr.nodelay(1)
		stdscr.addstr(int((console.HEIGHT-1)/2), int((console.WIDTH-16)/2), 'You lost a life!')
		stdscr.refresh()
		time.sleep(1)
	curses.wrapper(tempScr)
	score.add_lives(-1)
	if score.get_lives <= 0:
		return False
	else:
		return Snake(length = snake.length)

def highScores(score, name):
	try:
		f = open('highScores', 'rb')
		scores = pickle.load(f)
		if len(scores[0]) != 2:
			scores = []
		f.close()
	except:
		scores = []
	scores.append([name, score])
	f = open('highScores', 'wb')
	pickle.dump(scores, f)
	f.close()

def printHighScores(n=10, newScore=(0,0)):
	try:
		f = open('highScores', 'rb')
		scores = pickle.load(f)
		if len(scores[0]) != 2:
			scores = False
		f.close()
	except:
		scores = False
	if scores == False:
		print(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-24)/2)*' ' + 'No high scores in memory' + int(console.HEIGHT/2)*'\n')
	else:
		for iteration in range(len(scores)-1):
			swap = False
			for index in range(len(scores)-iteration-1):
				if scores[index][1] > scores[index+1][1]:
					swap = True
					current = scores[index]
					scores[index] = scores[index+1]
					scores[index+1] = current
			if not swap:
				break

		scores.reverse()
		scores = scores[:n]
		print(int((console.HEIGHT-len(scores))/2)*'\n')
		print(int((console.WIDTH-10)/2)*' ' + 'HIGHSCORES' + '\n')
		for i, score in enumerate(scores):
			if newScore[0] == score[0] and newScore[1] == score[1]:
				color = colorsText.GREEN
				print(int((console.WIDTH-30)/2)*' ' + colorsText.printout(str(i+1) + '. ' + score[0][:27-len(str(score[1]))] + (27-len(score[0]))*' ' + str(score[1]), color))
			else:
				print(int((console.WIDTH-30)/2)*' ' + str(i+1) + '. ' + score[0][:27-len(str(score[1]))] + (27-len(score[0]))*' ' + str(score[1]))
		print(int((console.HEIGHT-len(scores))/2)*'\n')

def menuScreen():
	goto = None
	while not goto == 'Start Game':
		goto = curses.wrapper(menu)
		if goto == 'High Scores':
			printHighScores()
			input('Press enter to continue')

def menu(stdscr):
	curses.start_color()
	curses.use_default_colors()
	curses.init_pair(1, curses.COLOR_GREEN, -1)
	curses.curs_set(0)
	stdscr.nodelay(0)
	n = curses.A_NORMAL
	h = curses.A_STANDOUT
	c = 0
	menuItems = ['Start Game', 'High Scores', 'Quit']
	pos = 1
	while not c == ord('\n'):
		stdscr.clear()

		def y(i):
			return int((console.HEIGHT-5)/2)+i
		def x(len):
			return int((console.WIDTH-len)/2)

		title = letters.word('snake!')
		line = ''
		lineNo = 0
		for letter in title:
			if letter == '\n':
				stdscr.addstr(y(-5+lineNo), x(len(line))+5, line, curses.color_pair(1))
				line = ''
				lineNo += 1
			else:
				line += letter
				
		for index, item in enumerate(menuItems):
			if pos == index+1:
				color = h
			else:
				color = n
			stdscr.addstr(y(index+2)+3, x(len(item) + len(str(index)) + 2), str(index+1) + '. ' + item, color)

		stdscr.refresh()
		c = stdscr.getch()

		if c == ord('1'):
			pos = 1
		elif c == ord('2'):
			pos = 2
		elif c == ord('3'):
			pos = 3
		elif c == 258:
			if pos < 3:
				pos += 1
			else:
				pos = 1
		elif c == 259:
			if pos > 1:
				pos -= 1
			else:
				pos = 3
		elif not c == ord('\n'):
			curses.flash()
		time.sleep(TICK)

	if pos == 3:
		print(int(console.HEIGHT)*'\n')
		sys.exit()
	else:
		return menuItems[pos-1]

def main(stdscr, score, snake):
	stdscr.nodelay(1)
	curses.curs_set(0)

	curses.start_color()
	curses.use_default_colors()
	curses.init_pair(1, curses.COLOR_RED, -1)
	curses.init_pair(2, curses.COLOR_GREEN, -1)
	curses.init_pair(3, curses.COLOR_BLACK, -1)

	grow = False
	food = Food(stdscr, snake, score)
	while True:
		stdscr.clear()

		c = stdscr.getch()

		if c == curses.KEY_RIGHT:
			snake.turn(True)
		if c == curses.KEY_LEFT:
			snake.turn(False)

		snake.screen(stdscr)
		snake.move(stdscr, grow)
		grow = food.update()
		stdscr.addstr(0, 0, 'Score: ' + score.print_score())
		stdscr.addstr(1, 0, 'Lives: ' + score.print_lives())
		stdscr.addstr(console.HEIGHT-1, 0, 'Press ESC to pause')

		stdscr.refresh()

		if c == 27:
			play = False
			win = curses.newwin(int(console.HEIGHT*.3), int(console.WIDTH*.3), int(console.HEIGHT*.35), int(console.WIDTH*.35))
			win.nodelay(1)
			char = 0
			while not char == 27:
				char = win.getch()
				win.clear()
				win.border(0)
				win.addstr(int(console.HEIGHT*.15)-1, int(console.WIDTH*.15)-5, 'Game Paused')
				win.addstr(int(console.HEIGHT*.15), int(console.WIDTH*.15)-10, 'Press ESC to continue')
				win.addstr(int(console.HEIGHT*.15)+1, int(console.WIDTH*.15)-7, 'Press Q to quit')
				win.refresh()
				if char == ord('q'):
					score.add_lives(-(score.get_lives-1))
					stdscr.addstr(console.HEIGHT*2, console.WIDTH*2, ' ')

				time.sleep(.1)

		time.sleep(TICK)

class Score(object):
	def __init__(self):
		self.score = 0
		self.lives = 3

	def print_score(self):
		return str(self.score)
	
	def print_lives(self):
		return str(self.lives)

	def add_score(self, amount):
		self.score += amount
	
	def add_lives(self, amount):
		self.lives += amount

	@property
	def get_lives(self):
		return self.lives

	@property
	def get_score(self):
		return self.score

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
	def __init__(self, x=console.WIDTH/2, y=console.HEIGHT/2, length=3, headType='O', bodyType='@'):
		self.body = []
		if length > console.WIDTH - 5:
			length = console.WIDTH - 5
		for xOff in range(length):
			self.body.append(Particle(y, x-xOff+length/2))
		self.direction = 0
		self.headType = headType
		self.bodyType = bodyType

	def move(self, stdscr, grow=False):
		x = self.x + int(math.sin(math.radians(self.direction*90)))
		y = self.y + int(math.cos(math.radians(self.direction*90)))

		self.body.insert(0, Particle(x, y))
		if not grow:
			self.body.pop(len(self.body)-1)

		for particle in self.body[1:]:
			if int(particle.x) == int(self.x) and int(particle.y) == int(self.y):
				1/0

	def turn(self, clkW):
		if clkW:
			self.direction += 1
		else:
			self.direction -= 1
		self.direction = self.direction % 4

	def screen(self, stdscr):
		for index, particle in enumerate(self.body):
			if particle == self.body[0]:
				char = self.headType
			else:
				char = self.bodyType

			if index == 0:
				stdscr.addstr(int(particle.x), int(particle.y), char, curses.color_pair(2))
			else:
				stdscr.addstr(int(particle.x), int(particle.y), char)

	@property
	def length(self):
		return len(self.body)

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
		if int(self.food.y) == int(self.snake.x) and int(self.food.x) == int(self.snake.y):
			self.new()
			self.score.add_score(1)
			grow = True
		else:
			grow = False
		self.stdscr.addstr(self.food.y, self.food.x, '#', curses.color_pair(1))
		return grow

menuScreen()
score, snake = init()

while not snake == False:
	print(console.HEIGHT*'\n')
	try:
		curses.wrapper(main, score, snake)
	except:
		try:
			time.sleep(.5)
			snake = die(snake, score)
			if snake == False:
				print(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-35)/2)*' ' + 'Game Over! You lost all your lives!\n')
				input(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-23)/2)*' ' + 'Press enter to continue' + int(console.HEIGHT/2)*'\n')
				response = input(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-40)/2)*' ' + 'Do you want to save your score? (YES/no)' + int(console.HEIGHT/2)*'\n')
				if not (response == 'no' or response == 'NO' or response == 'n' or response == 'N'):
					valid = False
					while not valid:
						name = input(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-16)/2)*' ' + 'Enter your name:' + int(console.HEIGHT/2)*'\n')
						if not name == '':
							valid = True
					highScores(score.get_score, name)
					printHighScores(newScore=(name,score.get_score))
					input('Press enter to continue')
				response = input(int(console.HEIGHT/2)*'\n' + int((console.WIDTH-32)/2)*' ' + 'Do you want to restart? (YES/no)' + int(console.HEIGHT/2)*'\n')
				if not (response == 'no' or response == 'NO' or response == 'n' or response == 'N'):
					score, snake = init()
				else:
					menuScreen()
					score, snake = init()
		except KeyboardInterrupt:
			print(console.HEIGHT*'\n')
			sys.exit()
