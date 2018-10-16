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
            while True:
                if sum == sum_one:
                    wins = wins + 1
                    break
                elif sum == 7:
                    pass
    return wins, games

def main():
    wins, games = craps()
    loses = int(games) - int(wins)
    percentage = int(wins)/int(games)
    print("You played ", games, "games. You won ", wins, "games and lost ", loses, "games.")
    print("You won ", percentage, "percent of the time.")


main()
