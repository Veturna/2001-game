import random


# xDy+z
# dice – he type of dice to be used (e.g. D6, D10)
# roll – number of dice throws; if we throw once, this parameter is negligible
# modifier - the number to add (or subtract) to the result of the throws (optional)


possible_dices = (
    "D100",
    "D20",
    "D12",
    "D10",
    "D8",
    "D6",
    "D4",
    "D3"
)


def roll_the_dices(code):
    for dice in possible_dices:
        if dice in code:
            try:
                roll, modifier = code.split(dice)
            except ValueError:
                return "Wrong input"
            type_of_dice = int(dice[1:])
            break
    else:
        return "Wrong input"

    try:
        roll = int(roll) if roll else 1
    except Exception:
        return "Wrong input"

    try:
        modifier = int(modifier) if modifier else 0
    except Exception:
        return "Wrong input"

    result = sum([random.randint(1, type_of_dice) for _ in range(roll)]) + modifier
    return result







