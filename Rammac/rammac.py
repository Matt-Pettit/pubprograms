#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rammac.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
#
#

import sys, os, random

def begin():
    try:
        option = str(sys.argv[1])
    except:
        print('You need to specify an option(-h for help)')
        exit()
    if option == '-r':
        change()
    if option == '-c':
        defaulter()

    if option == '-h':
        helper()

def inter():
    f = open('/home/matt/.config/rammac/config', 'r')
    f = f.readlines()
    interface = str(f[0])
    return(interface)


def defaulter():
    interface = str(input('Enter new interface name: '))
    f = open('/home/matt/.config/rammac/config', 'w+')
    f.write(interface)


def helper():
    print('Options are -r for a random MAC, -c to change the set Interface and -h for this dialouge')
    exit()

def maccer():
    first = '00:0F:1F:'
    rands = []
    for i in range(6):
        rands.append(random.randint(0,9))
    mac= first+str(rands[0])+str(rands[1])+':'+str(rands[2])+str(rands[3])+':'+str(rands[4])+str(rands[5])
    print(mac)
    return(mac)

def change():
    interface = inter()
    mac = maccer()
    os.system("ifconfig " + interface + " down")
    os.system("ifconfig " + interface + " hw ether "+mac)
    os.system("ifconfig " + interface + " up")
    os.system("nmcli radio wifi off")
    os.system("nmcli radio wifi on")



begin()
