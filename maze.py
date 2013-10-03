import time

grid = [['.','.','.','.','.','#'],
		['#','#','.','.','.','#'],
		['.','.','.','#','.','.'],
		['.','#','#','.','.','#'],
		['.','#','.','.','#','.'],
		['.','#','.','.','.','^']]

def search(x, y):
	if grid[x][y] == '^':
		return True
	elif grid[x][y] == '#':
		return False
	elif grid[x][y] == '+':
		return False

	grid[x][y] = '@'
	for line in reversed(grid):
		print ''.join(line)

	print ''
	time.sleep(0.2)

	# mark as visited
	grid[x][y] = '+'

	# explore neighbours clockwise starting by the one on the right
	if ((x < len(grid)-1 and search(x+1, y))
		or (y > 0 and search(x, y-1))
		or (x > 0 and search(x-1, y))
		or (y < len(grid)-1 and search(x, y+1))):
		return True

	return False

search(0, 0)
