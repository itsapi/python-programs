# a die simulator

import random, time


dots = {
    '1': '23456',
    '2': '',
    '3': '456',
    '4': '6',
    '5': '135',
    '6': '6',
    '7': '456',
    '8': '',
    '9': '23456'
}

i = 0

class Die:
    def __init__(self, char='#'):
        self.number = 0
        self.char = char

    def __str__(self):
        out = '╭' + ('─' * 7) + '╮\n'

        i = 0
        for row in range(3):
            out += '│ '
            for col in range(3):
                i += 1
                out += (self.char if str(self.number) in dots[str(i)] else ' ') + ' '
            out += '│\n'

        out += '╰' + ('─' * 7) + '╯\n'

        return out

    def roll(self):
        self.number = random.randint(1, 6)


die = Die('●')

while True:
    print(die)
    die.roll()
    input()
    time.sleep(0.1)
