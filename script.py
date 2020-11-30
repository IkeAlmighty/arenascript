import os, time, random

# runs a server command: 
def do_command(command):
    os.system('screen -S mc -p 0 -X stuff "{}\n"'.format(command))
    # for debugging:
    os.system('screen -S mc -p 0 -X stuff "say {}\n"'.format(command))

# data!
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

## CUSTOM FUNCTIONS ##

def lock_room(room_name, blocktype):
    # get the room:
    room = rooms[room_name]
    # first, figure out where each doorway is:
    x, y, z = room[0], room[1], room[2]
    doors = [
        (x + 4, y, z), 
        (x - 4, y, z), 
        (x, y, z + 4), 
        (x, y, z - 4)
    ]

    # then, for each door, fill it!
    for door in doors:
        x, y, z = door[0], door[1], door[2]
        do_command("fill {} {} {} {} {} {} minecraft:{}".format(x, y, z, x, y + 4, z, blocktype))

# for randl 'random list element'
def randl(_list):
    return _list[random.randint(0, len(_list) - 1)]

# TODO: this is not working because of quotations or something
def item_to_room(room_name, item, count):
    room = rooms[room_name]
    cmd_string = "summon minecraft:item {} {} {} {{Item:{{id:\"minecraft:{}\",Count:{}b}}}}"
    cmd = cmd_string.format(room[0], room[1], room[2], item, count)
    print(cmd)
    # os.system("echo {}".format(cmd))
    do_command(cmd_string.format(room[0], room[1], room[2], item, str(count)))

item_to_room("YELLOW", "stone_sword", 2)


## MAIN LOOP ##
def execute():
    do_command('give @a minecraft:{}'.format(randl(start_weapons)))
    do_command('give @a minecraft:{}'.format(randl(start_food)))
    lock_room("CENTER", "air")
    while True:
        # do_command('give @a minecraft:golden_apple')
        item_to_room("CENTER", "coal", 5)
        time.sleep(3)