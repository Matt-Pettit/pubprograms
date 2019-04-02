#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  codespammer.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
#
#
from pynput.keyboard import Key, Controller
keyboard = Controller()
import time



print("""

 ██████╗ ██████╗ ██████╗ ███████╗    ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗
██╔════╝██╔═══██╗██╔══██╗██╔════╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
██║     ██║   ██║██║  ██║█████╗      ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
██║     ██║   ██║██║  ██║██╔══╝      ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
╚██████╗╚██████╔╝██████╔╝███████╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
 ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝

By Matt Pettit

""")




mainlist = [1234,1111,"0000",1212,7777,1004,2000,4444,2222,6969,9999,3333,5555,6666,1122,1313,8888,4321,2001,1010]
global listofnums
listofnums = []


def sleeper():
    for i in range(5):
        print(str(5-i))
        time.sleep(1)


def e():
    keyboard.press("e")#presses e to reset code at end of code attempt
    keyboard.release("e")

def list():
    for i in range(10000): # main loop
        num = str(i)
        while (len(num) != 4): # loop to correctly format number
            num =  ("0"+num)
        listofnums.append(num)

def typer(word):
    e()
    for i in range(4): # bit that actually types out word
        time.sleep(0.1)
        keyboard.press(word[i])
        keyboard.release(word[i])

def main():
    sleep = int(input("How many secs rest before attempt(usually 20): "))
    sleeper()
    list()
    for item in mainlist:
        typer(str(item))
        time.sleep(sleep)
    for item in listofnums:
        typer(str(item))
        time.sleep(sleep)

main()
