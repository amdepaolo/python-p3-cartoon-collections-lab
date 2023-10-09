def roll_call_dwarves(names):
    for index, name in enumerate(names):
        print(f"{index + 1}. {name}")

def summon_captain_planet(list):
    yelling_list = [word.capitalize() + "!" for word in list]
    return yelling_list

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(foods):
    cheeses = ["cheddar", "gouds", "camembert"]
    for food in foods:
        if food in cheeses:
            return food
    return None
