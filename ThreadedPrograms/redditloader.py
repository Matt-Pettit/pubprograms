#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pageloader.py
#  
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
# 
# Requirements: wkhtmltopdf must be installed and geckodriver must be installed.  
#  
#
#
#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import random
import threading
global urls
urls = []
threads = []
subreddits = open("redditsubs.txt","r") 
redditurls = (subreddits.readlines())
print('To Do: '+str(len(redditurls))+' Subreddits')
global done
done = 0
global urlsfinal
urlsfinal = []
def lister(i):
	redditurl = redditurls[i]
	redditurl = redditurl[:-1]
	driver = webdriver.Firefox()
	driver.get(redditurl)
	elems = driver.find_elements_by_xpath("//a[@href]")
	for elem in elems:
		if "comments" in (str(elem.get_attribute("href"))):
			urls.append(elem.get_attribute("href"))
	driver.close()
	global done
	done += 1
	

def threader():	
	for i in range(len(redditurls)):
		t = threading.Thread(target=lister,args=(i,))
		threads.append(t)
		t.start()


def loader():
	while True:
		if done == len(redditurls):
			for i in range(len(urlsfinal)):
				currenturl = urlsfinal[i]
				print(currenturl)
				#os.system("wkhtmltopdf "+'"'+(urlss[i])+'"'+" "+str(ct)+".pdf")
				output = open("ouput.txt", "a")
				output.writelines(currenturl+'\n')
				output.close()
			break
		else:
			continue
		

def main():
	threader()
	
	loader()

main()


	
