import random
from collections import Counter
def roll_dice(num_dice):
    dice = []
    for i in range(num_dice):
        dice.append(random.randint(1, 6))
    return dice

def count_dice(dice, target):
    count = 0
    for num in dice:
        if num == target:
            count += 1
    return count

def get_duplicates(numbers):

    duplicates = Counter(numbers)

    duplicates = {value: count for value, count in duplicates.items() if count > 1}

    return duplicates

def play_perudo(num_dice, target_value):

    dice = roll_dice(num_dice)

    print("Выпавшие кубики:", dice)

    duplicates = get_duplicates(dice)
    if duplicates:
        print("В игре есть повторяющиеся кубики со значениями", duplicates)
    else:
        print("В игре нет повторяющихся кубиков")
    num_target = count_dice(dice, target_value)
    if num_target > 0:
        print("В игре есть кубики со значением", target_value)
    else:
        print("В игре нет кубиков со значением", target_value)

play_perudo(10, 4)
