import os, time

def do_command(command):
    os.system('screen -S mc -p 0 -X stuff "{}\n"'.format(command))

def execute():
    do_command('give @a minecraft:stone_sword')
    while True:
        do_command('give @a minecraft:golden_apple')
        time.sleep(20)