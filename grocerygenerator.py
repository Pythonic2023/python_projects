import random
import requests
import datetime as dt


def shuffle_list(main_dish, side_dish):
    """Shuffle our lists to have different foods for the week days"""
    random.shuffle(main_dish)
    random.shuffle(side_dish)
    return main_dish, side_dish


def finished_list(main, sides):
    """Print our finished list, if waffles make sides equal to bacon and
    hash brown"""
    # Provide chat id and token to message on telegram
    chat_id = ""
    token = ""
    todays_date = f"TODAY'S DATE: {dt.date.today()}"
    date_message = (f"https://api.telegram.org/bot{token}/sendMessage?chat_id="
                    f"{chat_id}&text={todays_date}")
    requests.get(date_message)
    for main, sides in zip(main[:7], sides):
        if main[:7] == 'waffles':
            sides = 'bacon hash brown'
            list_message = (f"https://api.telegram.org/bot{token}"
                            f"/sendMessage?chat_id={chat_id}&text={main}, {sides}")
            requests.get(list_message)
            print(f"{main} {sides}")
        else:
            print(f"{main} {sides}")
            message = (f"https://api.telegram.org/bot{token}"
                       f"/sendMessage?chat_id={chat_id}&text={main}, {sides}")
            requests.get(message)


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
