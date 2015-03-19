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

	if len(argv) == 1:
		print "random"
	elif str(argv[1]) == "random":
		print "random"
	elif str(argv[1]) == "view":
		view.data(argv)
	elif str(argv[1]) == "add":
		add.new(argv)
	elif str(argv[1]) == "remove":
		print "remove"
	elif str(argv[1]) == "rename":
		print "rename"
	elif str(argv[1]) == "merge":
		print "merge"
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

# first run
# make folder and file
print "Initialize ", version.now(), ", Please Wait..."
if not os.path.exists(config.listpath):
	if not os.path.exists(config.path):
		os.makedirs(config.path)
	try : 
		listfile = open(config.listpath, 'w')
		listfile.write(config.your_name + '\'s Amanat List:\n')
		listfile.close()
		print "Welcome, ", config.your_name
	except IOError, e:
		print "failed : ", e
else :
	print "Welcome Back, ",config.your_name
print "--------------------------------------------------"

exit = 0
fromdo = 0
menu(fromdo)
fromdo = 1
while not exit:
	print config.your_name, ": ",
	do.something()
	if str(do.argv[1]) == "exit" :
		break
	menu(fromdo)
print "Selamat Menjalankan Amanat"