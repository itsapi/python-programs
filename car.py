#coding=utf-8

import random
import math
import time
import console

class Game(object):
    def __init__(self):
        self.running = True
        self.money = 1000

        self.parts = {'engine' : 1,
                      'tyres' : 1,
                      'body' : 1}
        self.prices = {'engine' : 500,
                       'tyres' : 200,
                       'body' : 400}
        
        print '\n'*console.HEIGHT
        print self.car(' ')

    def menu(self, menuType):
        game.displayMoney()
        if menuType == 'main':
            print '1. Upgrade'
            print '2. Race'
            print '3. Exit'
            valid = False
            while not valid:
                choice = str(raw_input('Choose an option: '))
                if choice == '1':
                    print '\n'*console.HEIGHT
                    self.menu('upgrade')
                    valid = True
                elif choice == '2':
                    print '\n'*console.HEIGHT
                    self.race()
                    valid = True
                elif choice == '3':
                    print '\n'*console.HEIGHT
                    self.running = False
                    valid = True
        elif menuType == 'upgrade':
            print '1. Engine - Level ' + str(self.parts['engine']+1) + ' - £' + str(self.prices['engine'])
            print '2. Tyres - Level ' + str(self.parts['tyres']+1) + ' - £' + str(self.prices['tyres'])
            print '3. Body - Level ' + str(self.parts['body']+1) + ' - £' + str(self.prices['body'])
            print '4. Go Back'
            valid = False
            while not valid:
                choice = str(raw_input('Choose an option: '))
                if choice == '1':
                    print '\n'*console.HEIGHT
                    self.upgrade('engine')
                    valid = True
                elif choice == '2':
                    print '\n'*console.HEIGHT
                    self.upgrade('tyres')
                    valid = True
                elif choice == '3':
                    print '\n'*console.HEIGHT
                    self.upgrade('body')
                    valid = True
                elif choice == '4':
                    print '\n'*console.HEIGHT
                    valid = True

    def upgrade(self, part):
        if self.pay(self.prices[part]):
            self.parts[part] += 1
            print 'You bought the ' + part + ' upgrade for £' + str(self.prices[part]) + '.'
            print 'Your ' + part + ' is now upgraded to level ' + str(self.parts[part])
            self.prices[part] += self.prices[part] / 10
        else:
            print 'You cannot afford this upgrade'

    def displayMoney(self):
        print 'You have £' + str(self.money)

    def pay(self, amount):
        if self.money >= amount:
            self.money -= amount
            return True
        else:
            return False

    def race(self):
        # Calculating Winner
        opponentParts = {}
        for part in self.parts:
            opponentParts[part] = self.parts[part] + float(random.randint(0 - self.parts[part]*10, self.parts[part]*9))/100

        opponentLevel = 0;
        for part in opponentParts:
            opponentLevel += opponentParts[part]
        playerLevel = 0
        for part in self.parts:
            playerLevel += self.parts[part]

        # Prize Money
        prizeMoney = int(abs(round((playerLevel * random.randint(-playerLevel*10, playerLevel*10))/50)*50)+50)
        population = [i for i in range(50, 105)]
        population2 = [i for i in range(50, 75)]
        population += population2
        entryCost = prizeMoney*random.choice(population)/100

        print 'The entry cost for this race is £' + str(entryCost)
        print 'The prize for this race is £' + str(prizeMoney)

        cont = raw_input('Do you want to enter this race? (Y/n) ')
        if cont == 'Y' or cont == 'y' or cont == '':
            # Taking Entry Cost
            if not self.pay(entryCost):
                print '\n'*console.HEIGHT
                print 'You cannot afford the entry cost.'
            else:
                self.draw(playerLevel, opponentLevel)
                print '\n'*console.HEIGHT
                if opponentLevel > playerLevel:
                    # Opponent Wins
                    print 'You Lost!!'
                elif opponentLevel == playerLevel:
                    # Tie
                    print 'Tie!!'
                    print 'You got your £' + str(entryCost) + ' entry cost back'
                    self.money += entryCost
                else:
                    # Player Wins
                    print 'You Won £' + str(prizeMoney) + '!!'
                    self.money += prizeMoney
        else:
            print '\n'*console.HEIGHT
            print 'You quit the race.'

    def car(self, num, dist=0):
        if dist == 0 or 100-dist <= 8:
            spaceAfter = ''
        else:
            spaceAfter = (100-dist-8)*' ' + '|'
        return '{0} +--+   {1}\n{0}/  {2} \-o{1}\n{0}-O----O-{1}'.format(dist*' ', spaceAfter, num)

    def draw(self, player, opp):
        winnerSpeed = random.randint(5, 7)
        loserSpeed = random.randint(2, 4)
        if player > opp:
            speed = [winnerSpeed, loserSpeed]
            winnerCar = 0
        else:
            speed = [loserSpeed, winnerSpeed]
            winnerCar = 1
        winner = False
        n = 1
        while not winner:
            display = ''
            display += '\n'
            display += 'Player: 1\n'
            display += 'Opponent: 2\n'
            display += (console.HEIGHT/2-7)*('\n' + 100*' ' + '|') + '\n'
            display += self.car('1', n*speed[0]) + '\n'
            display += 100*' ' + '|\n'
            display += self.car('2', n*speed[1]) + '\n'
            display += (console.HEIGHT/2-5)*(100*' ' + '|' + '\n')
            if n*speed[winnerCar] >= 100:
                winner = True
            print display
            n += 1
            time.sleep(0.1)

game = Game()
while game.running:
    game.menu('main')
