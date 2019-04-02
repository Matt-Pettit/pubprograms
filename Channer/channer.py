# credits to Anarov for improved example - (used to find basic syntax of wrapper)

#"THE BEER-WARE LICENSE" (Revision 42):
#<pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
#can do whatever you want with this stuff. If we meet some day, and you think
#this stuff is worth it, you can buy me a beer in return. Matt Pettit

from __future__ import print_function
import basc_py4chan
import sys
import os

def start():	
	print("""
 ██████╗██╗  ██╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔════╝██║  ██║██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║     ███████║███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║     ██╔══██║██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
╚██████╗██║  ██║██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
 By Matt Pettit                                                           

""")
	
	try:
		decision = str(sys.argv[1]) 
		decision.lower()
		if decision == 'help':
			print('Options: board(will ask for board name, must be short name eg. "g" for Technology), boardlist(list of all 4Chan boards), thread(will ask for board and thread ID) and os(execute system commands)')
			decider()
		elif decision =='board':
			boarder()
		elif decision =='boardlist':
			boardnames()
		elif decision == 'thread':
			threader()
		
		elif decision == 'os':
			osrunner()
			
		else:
			print('Invalid option')
			decider()
	
	except:
		print("You should specify and option as an arguement(help for list of commands)")
		decider()

def decider():
	print('\nMAIN MENU:')
	decision = input('Enter option (help for list of commands): ')
	decision.lower()
	if decision == 'help':
		print('Options: board(will ask for board name, must be short name eg. "g" for Technology), boardlist(list of all 4Chan boards), thread(will ask for board and thread ID) and os(execute system commands)')
		decider()
	elif decision =='board':
		boarder()
	elif decision =='boardlist':
		boardnames()
	elif decision == 'thread':
		threader()
	elif decision == 'os':
			osrunner()
	else:
		print('Invalid option')
		decider()


def osrunner():
	command= (input('Command you would like to run("menu" to return to menu): '))
	if command == 'menu':
		decider()
	else:
		os.system(command)
		osrunner()	
			
	
def boardnames():
	print("""
 Japanese Culture:

    /a/ Anime and Manga
    /c/ Anime/Cute
    /w/ Anime/Wallpapers
    /m/ Mecha
    /cgl/ Cosplay and EGL
    /cm/ Cute/Male
    /f/ Flash
    /n/ Transportation
    /jp/ Otaku Culture
    /vp/ Pokemon

Interests:

    /v/ Video Games
    /vg/ Video Game Generals
    /vr/ Retro Games
    /co/ Comics & Cartoons
    /g/ Technology
    /tv/ Television & Film
    /k/ Weapons
    /o/ Auto
    /an/ Animals & Nature
    /tg/ Traditional Games
    /sp/ Sports
    /asp/ Alternative Sports
    /sci/ Science & Math
    /int/ International
    /out/ Outdoors
    /toy/ Toys
    /biz/ Business & Finance

Creative:

    /i/ Oekaki
    /po/ Papercraft & Origami
    /p/ Photography
    /ck/ Food & Cooking
    /ic/ Artwork/Critique
    /wg/ Wallpapers/General
    /mu/ Music
    /fa/ Fashion
    /3/ 3DCG
    /gd/ Graphic Design
    /diy/ Do-It-Yourself
    /wsg/ Worksafe GIF

Adult:

    /s/ Beautiful Women
    /hc/ Hardcore
    /hm/ Handsome Men
    /h/ Hentai
    /e/ Ecchi
    /u/ Yuri
    /d/ Hentai/Alternative
    /y/ Yaoi
    /t/ Torrents
    /hr/ High Resolution
    /gif/ Adult GIF

Other:

    /trv/ Travel
    /fit/ Fitness
    /x/ Paranormal
    /lit/ Literature
    /adv/ Advice
    /lgbt/ LGBT
    /mlp/ Pony [see My Little Pony]

Misc:

    /b/Random
    /r/ Request
    /r9k/ ROBOT9001
    /pol/ Politically Incorrect
    /soc/ Cams & Meetups
    /s4s/ Shit 4chan Says

""")
	decider()





def boarder():
	try:
		global board
		board = input('Enter the short version of the board you would like("menu" to go back to the menu): ')
		if board == 'menu':
			decider()
		else:
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
				print('Thred Thumbnail:',topic.thumbnail_url)
				print('-----------------------------------------------------------------\n')
				print('\n')
	except:
		print('There was an error(check your boardname)')
	decider()
			

def threader():
	try:	
		board = input('Enter the short version of the board you would like("menu" to go back to the menu): ')
		if board == 'menu':
			decider()
		else:
			board = basc_py4chan.Board(str(board))
			thread_id = input('Thread ID("menu" to go back to the menu): ')
			if thread_id == 'menu':
				decider()
			else:
				thread = board.get_thread(thread_id)
				topic = thread.topic
				print('Comment:\n', topic.text_comment)
				for i in range(len(thread.replies)):
					print(thread.replies[i].text_comment+'\n')
	except:
		print('There was an error(check your boardname)')		
	decider()

					



def main():
	start()

	
main()
	

