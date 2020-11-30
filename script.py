import os

screen = "mc"

def do_command(screen, command):
    os.system('screen -S {} -p 0 -X stuff "{}\n"'.format(screen, command))

def execute():
    do_command('say hello this is a test')
    pass