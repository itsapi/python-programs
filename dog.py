class Dog(object):
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.state = True

    def update(self):
        self.hunger -= 5
        if self.hunger <= 0:
            self.state = False

    def feed(self, amount):
        self.hunger += amount

    @property
    def dogName(self):
        return self.name

    @property
    def isAlive(self):
        return self.state

myDog = Dog('Name your dog: ')

while myDog.isAlive:
    myDog.update()
    myDog.feed(int(input('Feed ' + myDog.dogName)))
