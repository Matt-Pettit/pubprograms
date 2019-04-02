# credits to Anarov for improved example - (used to find basic syntax of wrapper)

#"THE BEER-WARE LICENSE" (Revision 42):
#<pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return. Matt Pettit

from __future__ import print_function
import basc_py4chan
import sys

print("""
     __       __
    / /_ _   / /
   / / _` | / / 
  / / (_| |/ /  
 /_/ \__, /_/   
     |___/      

 By Matt Pettit
""")


def boarder():
	try:
		
		board = 'g'
		board = basc_py4chan.Board(str(board))
		# select the first thread on the board
		all_thread_ids = board.get_all_thread_ids()
		amount = input('How many posts would you like?("all" for all posts on board): ')
		print('-----------------------------------------------------------------\n')
		if amount == 'all':
			amount = len(board.get_all_thread_ids())
		else: 
			amount = int(amount)
		for i in range(amount):
			thread_id = all_thread_ids[i]
			thread = board.get_thread(thread_id)
			print('Board:',board.title)
	
		# ~ # print thread information
		# ~ print(thread)
		# ~ print('Sticky?', thread.sticky)
		# ~ print('Closed?', thread.closed)
		
	
		# print topic post information
			topic = thread.topic
		# ~ print('Topic Repr', topic)
		# ~ print('Postnumber', topic.post_number)
			print('Timestamp', topic.timestamp)
		# ~ print('Datetime', repr(topic.datetime))
			print('Subject:', topic.subject)
			print('Comment:\n', topic.text_comment)
			print('URL:', topic.url)
			print('Replies:', len(thread.replies))
			print('Thread ID:',thread_id)
			print('Thread Thumbnail:',topic.thumbnail_url)
			print('-----------------------------------------------------------------\n')
			print('\n')
	except:
		print('There was an error(check your boardname)')
	threader()


def threader():
	try:	
		board = 'g'
		board = basc_py4chan.Board(str(board))
		thread_id = input('Thread ID(board to show board): ')
		if thread_id == 'board':
			boarder()
		else:
			thread = board.get_thread(thread_id)
			topic = thread.topic
			print('Comment:\n', topic.text_comment)
			for i in range(len(thread.replies)):
				print(thread.replies[i].text_comment+'\n')
	except:
		print('There was an error(check your boardname)')		
	threader


def main():
	boarder()
	threader()
	
main()
