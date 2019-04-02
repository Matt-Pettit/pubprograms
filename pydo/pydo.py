# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import sys


def load(option):
    try:
        linesr = []
        f = open('/home/matt/.pydo/pydo', 'r')
        lines = f.readlines()
        if option == 'r':
            if len(lines) == 1:
                print('You have', len(lines),'item on your todo list!')
            else:
                print('You have', len(lines),'items on your todo list!')
            for i in range(len(lines)):
                rem = (lines[i])[0:len(lines[i])-1]
                print((str(i+1)+')'+rem))
        if option == 'w':
            for i in range(len(lines)):
                linesr.append(lines[i])
            return(linesr)
        f.close()
    except:
        print('Either the file was not found or you dont have any reminders(try adding some).')


def adder():
    item = (input('Title: '))+'\n'
    f = open('/home/matt/.pydo/pydo', 'a')
    f.write(item)
    f.close()

def remover():
    lines = load('w')
    optionrem = int(sys.argv[2])
    lines.remove(lines[optionrem-1])
    f = open('/home/matt/.pydo/pydo', 'w')
    for line lines:
        f.write(line)
    f.close()
    load('r')

def help():
    print("""PyDo is a program written for reminders and todos.
    It has 4 options:
    -a add a reminder
    -l list current reminders
    -d remove a reminder(add reminder number after the -d)
    -h show this help messages
    """)

def start():
    try:
        option = str(sys.argv[1])
        if option == '-a':
            adder()
        if option == '-l':
            load('r')
        if option == '-d':
            remover()
        if (option == '-h') or (option == '-help') or (option == 'help'):
            help()
        if option == '':
            load('r')
    except:
        load('r')



start()
