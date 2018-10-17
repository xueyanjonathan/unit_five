# Jonathan Lin
# 10/17/2018
# For and While loops
# Using for and while loops to write a function modulling the craps game, and calculate the winning percentage

import random


def roll_a_dice():
    """
    This function modules a dice being rolled
    The points will be returned.
    :return: Points the user gets from rolling the dice.
    """
    return random.randint(1, 6)


def craps():
    """
    This function modules craps games which are played by the user for multiple times.
    The user inputs the times he or she wants to play the game.
    The function stores the number of wins among all games played.
    The function returns the number of wins and the total number of games.
    :return: number of wins and the total number of games.
    """
    wins = 0
    games = input("How many games do you want to play?")
    for x in range(int(games)):  # The beginning of the craps game.
        dice_one = roll_a_dice()
        dice_two = roll_a_dice()
        sum_one = dice_one + dice_two
        if sum_one == 7 or sum_one == 11:  # If the user gets 7 or 11 from the dices he or she rolls, the user wins.
            wins = wins + 1  # If the user wins, the total number of wins adds 1.
        elif sum_one == 2 or sum_one == 3 or sum_one == 12:
            pass  # The user loses.
        else:  # The user continues rolling until they roll the point(sum_one) again (they win)
            # or they roll a 7 (they lose).
            while True:
                dice_three = roll_a_dice()
                dice_four = roll_a_dice()
                sum = dice_three + dice_four
                if sum == sum_one:
                    wins = wins + 1
                    break  # The user wins and stops rolling the dice.
                elif sum == 7:
                    break  # The user loses and stops rolling the dice.
    return wins, games


def main():
    wins, games = craps()
    loses = int(games) - int(wins)
    percentage = int(wins)/int(games) * 100
    print("You played", games, "games. You won", wins, "games and lost", loses, "games.")
    print("You won", percentage, "percent of the time.")


main()
