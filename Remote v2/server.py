#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  server.py
#
#  Copyright 2018 Matt Pettit <pettit.matt@gmail.com>
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#


import socket

s = socket.socket()
host = "localhost"
port = 1213
s.bind((host,port))
s.listen(5)

c, addr = s.accept()
print("Connection accepted from ")

c.send((input("What would you like to send? ")).encode())

c.close()
