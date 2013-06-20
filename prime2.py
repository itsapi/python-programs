import sys
import time

def primes(n): 
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

now = time.time()
primes = primes(int(sys.argv[1]))
time = time.time()-now
print('Found ' + str(len(primes)) + ' primes under ' + sys.argv[1] + ' in ' + str(int(time*1000)) + ' ms')