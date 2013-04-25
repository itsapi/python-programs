pi = float(0)
n = float(1)

while True:
	pi += 4 * (((-1)**(n+1))/((2*n)-1))
	n += 1
	print pi
