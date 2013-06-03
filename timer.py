import time
import datetime

hours = input('How many hours? ')
mins = input('How many minutes? ')
secs = input('How many seconds? ')

print('')

len = (mins*60)+(hours*60*60)+secs
now = time.time()

for i in range(len):
	elapsed = time.time()-now
	remaining = len-elapsed

	mE, sE = divmod(elapsed, 60)
	hE, mE = divmod(mE, 60)
	mR, sR = divmod(remaining, 60)
	hR, mR = divmod(mR, 60)

	print('Elapsed: ' + '%d:%02d:%02d' % (hE, mE, sE) + '	Remaining: ' + '%d:%02d:%02d' % (hR, mR, sR))
	time.sleep(1)

print("\nTIME'S UP!")
