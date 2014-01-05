import sys
import time

def isPrime(n):
	n = abs(n)
	if (n == 0 or n == 1):
		return 0
	if (n == 2):
		return 1
	if (n%2 == 0):
		return 0
	if (n<9):
		return 1
	
	i = 3

	while (i < n**0.5):
		if (n%i == 0):
			return 0
		i = i+2

	return 1

now = time.time()
primes = []
i = 0

while (i < int(sys.argv[1])):
	if (isPrime(i)):
		# print(str(i) + ' is prime - ' + str(len(primes)) + ' primes found')
		primes.append(i)
	i += 1

time = time.time()-now
print('Found ' + str(len(primes)) + ' primes under ' + str(i) + ' in ' + str(int(time*1000)) + ' ms')