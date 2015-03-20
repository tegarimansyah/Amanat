#!/bin/usr/env python
import os
import sys
from amanat import *

def menu(fromdo):	
	# check argument
	if not fromdo:
		argv = sys.argv
	else :
		argv = do.argv

	if len(argv) <= 1 :
		rando.rando()
	elif str(argv[1]) == "random":
		rando.rando()
	elif str(argv[1]) == "view":
		view.data(argv)
	elif str(argv[1]) == "add":
		add.new(argv)
	elif str(argv[1]) == "remove":
		remove.remove()
	elif str(argv[1]) == "rename":
		rename.rename()
	elif str(argv[1]) == "merge":
		merge.merge()
	elif str(argv[1]) == "help":
		help.me()
	elif str(argv[1]) == "version":
		print version.now()
	elif str(argv[1]) == "about":
		if len(argv) == 3 and str(argv[2]) == "all" :
			about.all()
		else :
			about.short()
	else :
		print ("Wrong Options")

def firstrun():
	if not os.path.exists(_config.path):
		os.makedirs(_config.path)
	try : 
		listfile = open(_config.listpath, 'w')
		listfile.write("0 " + _config.your_name + '\'s Amanat List:\n')
		listfile.close()
		print "Welcome, ", _config.your_name
	except IOError, e:
		print "failed : ", e
# first run
# make folder and file
if os.name == 'nt':
	os.system('cls')
else:
	os.system('clear')
print "Initialize ", version.now(), ", Please Wait..."
if not os.path.exists(_config.listpath):
	firstrun()
else :
	print "Welcome Back, ",_config.your_name

print "--------------------------------------------------"
exit = 0
fromdo = 0
menu(fromdo)
fromdo = 1
while not exit:
	print _config.your_name, ": ",
	do.something()
	if len(do.argv) > 1 and str(do.argv[1]) == "exit" :
		break
	menu(fromdo)
print "Selamat Menjalankan Amanat"