import random

games = input("How many times do you want to play?")

def craps():
    for x in range(int(games)):
        roll_a_dice = random.randint(1,6)
        dice_one = roll_a_dice
        dice_two = roll_a_dice
        sum_one = dice_one + dice_two
        print("You rolled a", dice_one, " and a", dice_two, ". Your sum is", sum_one, ".")
        if sum == 7 or sum == 11:
            print("You win.")
        elif sum == 2 or sum == 3 or sum == 12:
            print("You lose.")
        else:
            dice_three = roll_a_dice
            dice_four = roll_a_dice
            sum = dice_three + dice_four

def main():
