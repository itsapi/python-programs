class Puzzle(object):
	def __init__(self, arg):
		self.arg = arg

class Cell(object):
	def __init__(self, arg):
		self.arg = arg
		
def main():
	# Extracts puzzles from file and puts them into an array
	f = open('sudoku_file', 'r')
	puzzles = []
	for line in f:
		puzzles.append(line[:-2])
	f.close()

	puzzle = Puzzle(puzzles[0])

	while not puzzle.solved:
		