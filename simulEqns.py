import math

class Equation(object):
	def __init__(self):
		print('y=mx+c')
		valid = False
		while not valid:
			valid = True
			self.m = eval(input('Enter the value for m: '))
			self.c = eval(input('Enter the value for c: '))
			try:
				self.m = int(self.m)
				self.c = int(self.c)
			except ValueError:
				valid = False
				print('Error in input')

def solve(eq1, eq2):
	m = eq1.m + (-1*eq2.m)
	c = eq1.c + (-1*eq2.c)
	if m == 0:
		x = -c
	else:
		x = (-c)/m
	y = (eq1.m*x) + eq1.c
	print(('\nX = '+str(x)+', Y = '+str(y)+'\n'))

while True:
	print('Equation 1:')
	eq1 = Equation()
	print(('y='+str(eq1.m)+'x+'+str(eq1.c)))
	print('\nEquation 2:')
	eq2 = Equation()
	print(('y='+str(eq2.m)+'x+'+str(eq2.c)))
	print('\nSolving:')
	print((solve(eq1, eq2)))
