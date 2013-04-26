import time

class Game(object):
    def __init__(self):
        pass
    def start(self, length):
        old_time = time.time()
        eval(input('Is time up yet?'))
        diff = time.time() - old_time
        if round(diff, 1) == length:
            print('Bang on!')
        else:
            print(('You were ' + str(round(abs(length - diff), 1)) + ' seconds out.'))

g = Game()
