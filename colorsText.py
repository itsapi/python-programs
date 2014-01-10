import sys

BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = list(range(8))

def has_colors(stream):
	if not hasattr(stream, 'isatty'):
		return False
	if not stream.isatty():
		return False
	try:
		import curses
		curses.setupterm()
		return curses.tigetnum('colors') > 2
	except:
		return False

has_colors = has_colors(sys.stdout)

def printout(text, color=WHITE):
	if has_colors:
		seq = '\x1b[1;%dm' % (30+color) + text + '\x1b[0m'
		return seq
	else:
		return text
