# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


from __future__ import print_function
import basc_py4chan
import sys
import os
import threading
import time
board = basc_py4chan.Board(str('g'))
# select the first thread on the board
all_thread_ids = board.get_all_thread_ids()
mainlist = []
threads = []



def boarder(i):
    thread_id = all_thread_ids[i]
    thread = board.get_thread(thread_id)
    topic = thread.topic
    mainlist.append('Subject:'+str(topic.subject))
    mainlist.append('Comment:'+str(topic.text_comment))
    mainlist.append('Replies:'+str(len(thread.replies)))
    mainlist.append('Thread ID:'+str(thread_id))
    mainlist.append('------------------------------------------------------')


for i in range(150):
	t = threading.Thread(target=boarder,args=(i,))
	threads.append(t)
	t.start()
time.sleep(3)
for item in mainlist:
    print(item)
print(len(mainlist)/5)
