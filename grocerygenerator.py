import random
import requests
import datetime as dt


def shuffle_list(main_dish, side_dish):
    """Shuffle our lists to have different foods for the week days"""
    random.shuffle(main_dish)
    random.shuffle(side_dish)
    return main_dish, side_dish


def send_date():
    chat_id = ""
    token = ""
    todays_date = f"TODAY'S DATE: {dt.date.today()}"
    date_message = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id="
                    f"{chat_id}&text={todays_date}")
    requests.get(date_message)


def send_message(forward_list):
    chat_id = ""
    token = ""
    list_message = (f"https://api.telegram.org/bot{token}"
                    f"/sendMessage?chat_id={chat_id}&text={forward_list}")
    requests.get(list_message)


def finished_list(finish_main, finish_sides):
    """Print our finished list, if waffles make sides equal to bacon and
    hash brown"""
    food_list = []
    for main_dish, side_dish in zip(finish_main[:7], finish_sides):
        if 'waffles' in main_dish[:7]:
            waffle_bacon_hash = f"waffles, bacon and hashbrown"
            food_list.append(waffle_bacon_hash)
            continue
        else:
            meal = f"{main_dish} {side_dish}"
            food_list.append(meal)

    our_finished_list = '\n'.join(food_list)
    return our_finished_list


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
returned_list = finished_list(main, sides)
send_date()
send_message(returned_list)
