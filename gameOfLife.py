import console
import sys
import time
from copy import *
from random import *

def read_seed():
	#open given seed file
	f = open(sys.argv[1],'r')
	seed_ = f.readlines()

	#manipulate to correct form
	seed_ = [x for x in seed_ if not x.startswith('!')]
	seed = [[0 for i in seed_[0]] for i in seed_]
	for y,row in enumerate(seed_):
		for x,cell in enumerate(row):
			seed[y][x] = 1 if cell == 'O' else 0
	return seed

def create_frame():
	#create frame with all zeros
	frame = [[0 for i in range(width)] for i in range(height)]

	#insert seed into centre of frame
	for j,y in enumerate(range(int((height-len(seed))/2),int((height+len(seed))/2))):
		for i,x in enumerate(range(int((width-len(seed[0]))/2),int((width+len(seed[0]))/2))):
			frame[y][x] = seed[j][i]
	return frame

def is_alive(x,y):
	#return state of given cell
	return frame[y%height][x%width]

def check_cells(x,y):
	#count number of alive cells surrounding
	number = -1
	for yOff in range(-1,2):
		for xOff in range(-1,2):
			number += is_alive(x+xOff,y+yOff)

	#change state of cell depending on number of alive cells surrounding
	if frame[y][x]:
		if number < 2:
			#any live cell with fewer than two live neighbours dies, as if caused by under-population.
			new_frame[y][x] = 0
		elif number < 4:
			#any live cell with two or three live neighbours lives on to the next generation.
			new_frame[y][x] = 1
		else:
			#any live cell with more than three live neighbours dies, as if by overcrowding.
			new_frame[y][x] = 0
	else:
		if number == 2:
			#any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
			new_frame[y][x] = 1

#program start
width = console.WIDTH
height = console.HEIGHT
seed = read_seed()
frame = create_frame()

while True:
	#print frame
	for row in frame:
		for cell in row:
			out = '#' if cell else ' '
			print(out,end='')
		print()
	print()

	#check cells using rules
	new_frame = deepcopy(frame)
	for y, row in enumerate(frame):
		for x, cell in enumerate(row):
			check_cells(x,y)
	frame = new_frame

	time.sleep(0.1)