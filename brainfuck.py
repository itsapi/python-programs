import sys

data = open('brainfucksrc', 'r').read()
out = ''
dataPointer = 0
instructionPointer = 0
cells = [0]*30000

while instructionPointer < len(data):
    if data[instructionPointer] == '+':
        cells[dataPointer] += 1
    elif data[instructionPointer] == '-':
        cells[dataPointer] -= 1
    elif data[instructionPointer] == '>':
        dataPointer += 1
    elif data[instructionPointer] == '<':
        dataPointer -= 1
    elif data[instructionPointer] == '.':
        out += chr(cells[dataPointer])
        if cells[dataPointer] == 0:
        	print(out)
        	out = ''
    elif data[instructionPointer] == ',':
        cells[dataPointer] = ord(raw_input('input character: '))
    elif data[instructionPointer] == '[':
        if cells[dataPointer] == 0:
            nest = 1
            while nest > 0:
                instructionPointer += 1
                if data[instructionPointer] == '[':
                    nest += 1
                elif data[instructionPointer] == ']':
                    nest -= 1
    elif data[instructionPointer] == ']':
        if cells[dataPointer] != 0:
            nest = 1
            while nest > 0:
                instructionPointer -= 1
                if data[instructionPointer] == ']':
                    nest += 1
                elif data[instructionPointer] == '[':
                    nest -= 1
    instructionPointer += 1
if out != '':
	print(out)