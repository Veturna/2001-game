import random


def user_move():
    points = 0
    move = input("Click enter to roll the dice!")
    round = 1
    dice = 0

    if move == "":
        for _ in range(2):
            dice += random.randint(1, 6)
    print (dice)

user_move()

