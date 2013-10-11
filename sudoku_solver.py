class Puzzle(object):
	def __init__(self, puzzle):
		self.puzzle = [Cell(num, (int(i/9), i%9)) for i, num in enumerate(puzzle)]
	
	def __str__(self):
		# Print sudoku grid with numbers
		out = '\n'
		for y, row in enumerate(self.puzzle):
			for x, cell in enumerate(row):
				if x%3 == 0:
					out += '| '
				out += str(cell) + ' '
			if (y+1)%3 == 0:
				out += '\n' + ('-'*24)
			out += '\n'
		return out

class Cell(object):
	def __init__(self, num, pos):
		self.num = int(num)
		if self.num == 0:
			self.candidates = [i for i in range(1, 10)]
		else:
			self.candidates = [num]
		self.pos = pos
		
	def __str__(self):
		if self.num == 0:
			return ' '
		else:
			return str(self.num)
		
def main():
	# Extracts puzzles from file and puts them into an array
	f = open('sudoku_file', 'r')
	puzzles = []
	for line in f:
		puzzles.append(line[:-2])
	f.close()

	puzzle = Puzzle('000150320000000050408009000000008004000000000023000000800005000000000000037200010')
	print(puzzle)

	while not puzzle.solved:
		pass
		
main()
