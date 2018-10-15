import random


def craps():
    roll_a_dice = random.randint(1, 6)
    wins = 0
    games = input("How many games do you want to play?")
    for x in range(int(games)):
        dice_one = roll_a_dice
        dice_two = roll_a_dice
        sum_one = dice_one + dice_two
        if sum_one == 7 or sum_one == 11:
            wins = wins + 1
        elif sum_one == 2 or sum_one == 3 or sum_one == 12:
            pass
        else:
            dice_three = roll_a_dice
            dice_four = roll_a_dice
            sum = dice_three + dice_four
            while sum != sum_one or sum != 7:
                dice_three = roll_a_dice
                dice_four = roll_a_dice
                sum = dice_three + dice_four
        return wins, games


def main():
    wins, games = craps()
    percentage = wins/games
    print("You ")
    print("You won ", percentage, "percent of the time.")
