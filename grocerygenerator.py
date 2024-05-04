import random


def shuffle_list(main_dish, side_dish):
    """Shuffle our lists to have different foods for the week days"""
    random.shuffle(main_dish)
    random.shuffle(side_dish)
    return main_dish, side_dish


def finished_list(main, sides):
    """Print our finished list, if waffles make sides equal to bacon and hash brown"""
    for main, sides in zip(main[:7], sides):
        if main == 'waffles':
            sides = 'bacon hash brown'
            print(f"{main} {sides}")
        print(f"{main} {sides}")


# Main dishes
main = [
    'chicken burgers',
    'pizza',
    'steak',
    'hot dogs',
    'chicken breast',
    'grilled cheese',
    'pork chops',
    'waffles',
]
# Side dishes
sides = [
    'fries',
    'cesar salad',
    'fries',
    'cesar salad',
    'fries',
    'cesar salad',
    'fries',
    'cesar salad',
]
# Call our shuffle function, store tuple of lists into grocery list
grocery_list = shuffle_list(main, sides)
# Populate our main list with the shuffled values
main = grocery_list[0]
# Populate our sides list with the shuffled values
sides = grocery_list[1]
# Call on finished_list to present the final menu
finished_list(main, sides)