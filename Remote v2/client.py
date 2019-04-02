#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  client.py
#
#  Copyright 2018 Matt Pettit <pettit.matt@gmail.com>
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#

interface = ""

import socket
while True:
	try:
		global mac
		s = socket.socket()
		host = 'localhost' # needs to be in quote
		port = 1213
		s.connect((host, port))
		put = str((s.recv(1024)))
		mac = str(put[2: (len(put)-1)])
		print(mac)
		maccer()
	except:
		continue

def maccer():
	while True:

		os.system("ifconfig " + interface + " down")
		os.system("ifconfig " + interface + " hw ether "+mac)
		os.system("ifconfig " + interface + " up")
		os.system("nmcli radio wifi off")
		os.system("nmcli radio wifi on")
