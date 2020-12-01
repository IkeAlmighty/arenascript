import os, time, random

# runs a server command: 
def do_command(command):
    os.system('screen -S mc -p 0 -X stuff "{}\n"'.format(command))
    # for debugging:
    # os.system('screen -S mc -p 0 -X stuff "say {}\n"'.format(command))

# data!
start_weapons = ["stone_axe", "stone_pickaxe", "stone_sword", "diamond_sword"]
food = ["golden_apple", "apple", "cooked_beef", "cooked_chicken"]
blocks = [
    "white_wool", 
    "snow_block",  
    "crafting_table", 
    "crafting_table", 
    "furnace", 
    "acacia_planks",
    "red_wool",
    "stone",
    "acacia_door",
    "iron_door",
    "redstone",
    "lever",
    "brewing_stand",
    "brick_wall",
    "oak_log"
    ]
items = [
    "iron_pickaxe", 
    "iron_axe", 
    "stick", 
    "blue_bed",
    "flint_and_steel",
    "creeper_spawn_egg",
    "wolf_spawn_egg",
    "tnt",
    "torch",
    "soul_torch",
    "iron_sword",
    "diamond_sword"
    ]
mobs = ["blaze", "skeleton", "creeper", "zombie", "witch", "villager"]

rooms = {
    "CENTER": (8, 4, 8),
    "ORANGE": (0, 4, 8),
    "GREEN": (8, 4, 0),
    "CYAN": (16, 4, 8),
    "PINK": (16, 4, 0),
    "YELLOW": (8, 4, 0),
    "BLUE": (0, 4, 0),
    "PURPLE": (8, 4, 16),
    "RED": (16, 4, 16)
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

    # reset the arena
    # fill air -9 0 -9 25 10 25
    # clone -9 107 -9 25 100 25 -9 2 -9 
    do_command("fill -9 0 -9 25 10 25 minecraft:air")
    time.sleep(3)
    do_command("clone -9 107 -9 25 100 25 -9 2 -9")

    do_command('kill @e')
    do_command('clear @a')

    lock_room("CENTER", "obsidian")
    x, y, z = rooms["CENTER"][0], rooms["CENTER"][1], rooms["CENTER"][2]
    do_command('tp @a {} {} {}'.format(x, y, z))

    do_command('give @a minecraft:{}'.format(randl(start_weapons)))
    do_command('give @a minecraft:{}'.format(randl(food)))

    for second in range(10):
        time.sleep(1)
        do_command('say beginning in {}'.format(11 - second))

    lock_room("CENTER", "air")
    do_command("give @a minecraft:{}".format(randl(start_weapons)))
    do_command("give @a minecraft:{}".format(randl(items)))
    do_command("give @a minecraft:{}".format(randl(items)))

    for round_num in range(20):
        time.sleep(3) #for drama
        do_command('say round {}'.format(round_num))

        time.sleep(40)
        do_command('give @r minecraft:golden_apple')
        for i in range(10):
            time.sleep(1)
            do_command('say {}'.format(10 - i))
        
        # lock and unlock rooms randomly:
        lock_room(randl(list(rooms.keys())), "obsidian")
        lock_room(randl(list(rooms.keys())), "obsidian")
        lock_room(randl(list(rooms.keys())), "obsidian")
        lock_room(randl(list(rooms.keys())), "obsidian")
        lock_room(randl(list(rooms.keys())), "air")
        lock_room(randl(list(rooms.keys())), "air")
        lock_room(randl(list(rooms.keys())), "air")

        # give random players items:
        do_command("give @r minecraft:{}".format(randl(items)))
        do_command("give @r minecraft:{} {}".format(randl(blocks), random.randint(3, 7)))
        do_command("give @r minecraft:{}".format(randl(food)))
        do_command("xp add @r {}".format(random.randint(20, 70)))

        # summon a mob to a random room:
        rand_room = randl(list(rooms.keys()))
        x, y, z = rand_room[0], rand_room[1], rand_room[2]
        do_command("summon minecraft:{} {} {} {}".format(randl(mobs), x, y, z))
    
    # cleanup

