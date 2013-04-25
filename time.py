import time
import sys
import console
import letters
import os

while True:
	text = ''

	for char in os.popen('date').read():
                if char != '\n' and char != '\t':
                        text += char

	text = letters.word(text)

	lines = []
	line = ''
	for char in text:
		line += char
		if char == '\n':
			lines.append((' '*console.WIDTH) + line[:len(line)-1])
			line = ''

	i = 0
	for i in range(len(lines[0])):
		print '\n'*(console.HEIGHT/2-2)
		for line in lines:
			print (line[i % len(line):] + line[:i % len(line)])[:console.WIDTH]
		print '\n'*(console.HEIGHT/2-3)
		i += 1
		time.sleep(.02)
