# a die simulator

import random, time


dots = {
    '0': '',
    '1': '5',
    '2': '19',
    '3': '159',
    '4': '1379',
    '5': '13579',
    '6': '134679'
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
                out += (self.char if str(i) in dots[str(self.number)] else ' ') + ' '
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
