import pickle

try:
	f = file('anotherMyOtherFile', 'w+r')
	pickle.dump(['olls', 20000], f)
	f.close()
	print hello
except:
	print 'hello'
