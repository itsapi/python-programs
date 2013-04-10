import random
num = random.randint(1,100)
num2 = int(input("Guess my number between 1 and 100: "))
while num2 != num:
    if num2>num:
        num2 = int(input("lower: "))
    else:
        num2 = int(input("higher: "))
print ("You guessed the number!")
