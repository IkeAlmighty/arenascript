import os, time, random

start_weapons = ["stone_axe", "stone_pickaxe", "stone_sword", "diamond_sword"]
start_food = ["golden_apple", "apple", "cooked_beef", "cooked_chicken"]

rooms = {
    "CENTER": (8, 3, 8),
    "ORANGE": (0, 3, 8),
    "GREEN": (8, 3, 0),
    "CYAN": (16, 3, 8),
    "PINK": (16, 3, 0),
    "YELLOW": (8, 3, 0),
    "BLUE": (0, 3, 0),
    "PURPLE": (8, 3, 16),
    "RED": (16, 3, 16)
}

def lock_room():
    pass

# for randl 'random list element'
def randl(_list):
    return _list[random.randint(0, len(_list) - 1)]

def item_to_room(room_name, item, count):
    room = rooms[room_name]
    cmd_string = 'summon minecraft:item {} {} {} {{Item:{{id:"minecraft:{}",Count:{}b}}}}'
    do_command(cmd_string.format(room[0], room[1], room[2], item, str(count)))

## MAIN COMMANDS ##
def do_command(command):
    os.system('screen -S mc -p 0 -X stuff "{}\n"'.format(command))

def execute():
    do_command('give @a minecraft:{}'.format(randl(start_weapons)))
    do_command('give @a minecraft:{}'.format(randl(start_food)))

    while True:
        # do_command('give @a minecraft:golden_apple')
        item_to_room("CENTER", "coal", 5)
        time.sleep(3)