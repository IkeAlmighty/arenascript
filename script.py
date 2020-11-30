import os

def do_command(command):
    os.system('screen -S mc -p 0 -X stuff "{}\n"'.format(screen, command))

def execute():
    do_command('say hello this is a test')
    pass