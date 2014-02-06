import sys
import random

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

answer = 0
while not answer*num2 == num1:
    answer = random.randint(0, 10000)

print('{} / {} = {}'.format(num1, num2, answer))
