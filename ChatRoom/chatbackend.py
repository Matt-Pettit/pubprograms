#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  chatbackend.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
# Python program to implement server side of chat room.
import socket
import select
import sys
from thread import *

"""The first argument AF_INET is the address domain of the
socket. This is used when we have an Internet Domain with
any two hosts The second argument is the type of socket.
SOCK_STREAM means that data or characters are read in
a continuous flow."""
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided


# takes the first argument from command prompt as IP address
IP_address = str(raw_input('Enter IP: '))

# takes second argument from command prompt as port number
Port = int(10001)
"""
binds the server to an entered IP address and at the
specified port number.
The client must be aware of these parameters
"""
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
server.listen(100)

list_of_clients = []

def clientthread(conn, addr):
    history = open("history.txt","r")
    # sends a message to the client whose user object is conn
    conn.send("Welcome to this chatroom! We Allow for you to enter your real name but for privacy reasons it is not compulsory, feel free to make it something fun\n")
    for line in history:
        conn.send(line)


    while True:
            history = open("history.txt","a")
            try:
                message = conn.recv(2048)
                if message:

                    """prints the message and address of the
                    user who just sent the message on the server
                    terminal"""
                    history.write(message+'\n')
                    history.close
                    print (message)

                    # Calls broadcast function to send message to all
                    message_to_send =(message)
                    broadcast(message_to_send, conn)



            except:
                continue

"""Using the below function, we broadcast the message to all
clients who's object is not the same as the one sending
the message """
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message)
            except:
                clients.close()

                # if the link is broken, we remove the client
                remove(clients)

"""The following function simply removes the object
from the list that was created at the beginning of
the program"""
def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

while True:

    """Accepts a connection request and stores two parameters,
    conn which is a socket object for that user, and addr
    which contains the IP address of the client that just
    connected"""
    conn, addr = server.accept()

    """Maintains a list of clients for ease of broadcasting
    a message to all available people in the chatroom"""
    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print("Someone connected")

    # creates and individual thread for every user
    # that connects
    start_new_thread(clientthread,(conn,addr))

conn.close()
server.close()
