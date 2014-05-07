# a die simulator

import random, time


numbers = {
    '0': [
        '   ',
        '   ',
        '   '
    ],
    '1': [
        '   ',
        ' # ',
        '   '
    ],
    '2': [
        '#  ',
        '   ',
        '  #'
    ],
    '3': [
        '#  ',
        ' # ',
        '  #'
    ],
    '4': [
        '# #',
        '   ',
        '# #'
    ],
    '5': [
        '# #',
        ' # ',
        '# #'
    ],
    '6': [
        '# #',
        '# #',
        '# #'
    ],
}

class Die:
    def __init__(self, char='#'):
        self.number = 0
        self.char = char

    def __str__(self):
        face = numbers[str(self.number)]
        out = '╭' + ('─' * 7) + '╮\n'

        for row in face:
            out += '│ '
            for char in row:
                out += (self.char if char == '#' else ' ') + ' '
            out += '│\n'
                
        out += '╰' + ('─' * 7) + '╯\n'
        
        return out

    def roll(self):
        self.number = random.randint(1, 6)


die = Die('●')

while True:
    print(die)
    die.roll()
    time.sleep(0.1)
