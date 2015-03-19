#!/bin/usr/env python
from __future__ import print_function
import os
import sys
import mmap
import about


# config
your_name = "Tegar Imansyah"
path = "../coba/"
listpath = path + "list.txt"

# first run
# make folder and file
if not os.path.exists(listpath):
	if not os.path.exists(path):
		os.makedirs(path)
	try : 
		listfile = open(listpath, 'w')
		listfile.write(your_name + '\'s Amanat List:\n')
		listfile.close()
	except IOError, e:
		print ("failed : ", e)

# random
def random():
	print ("random function")

# view
def view():
	listfile = open(listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_READ)
	error = 0
	i = 0
	while search[i] != ":":
		i += 1	
	if len(sys.argv) == 2 : # amanat.py view
		print ("Display exists person:")
		j = i + 1
		while  j < os.fstat(listfile.fileno()).st_size: # prevent EOF
			if search[j] >= "a" and search[j] <= "z" or search[j] >= "A" and search[j] <= "Z" :
				print (search[j],end='')				
			j += 1
		search.seek(0)	
		nama = str(raw_input("\nchoose person: ")) # can make more than 1 word
		# number = int(raw_input("Write the message: "))
	elif len(sys.argv) == 3 : # amanat.py view name
		nama = str(sys.argv[2])
		# message = str(raw_input("Write the message\n\n"))
	elif len(sys.argv) == 4 : # amanat.py view name number
		nama = str(sys.argv[2])
		# message = str(sys.argv[3])
	else :
		print ("your argument is too much")
		error = 1

	if not error and os.path.exists(path + nama + ".txt"):
		namafile = open(path + nama + ".txt", 'a+')
		namafiles = mmap.mmap(namafile.fileno(), 0, access=mmap.ACCESS_READ)
		j = 0
		pesanke = 1
		print(nama," said that :\n\n",pesanke,". ",end="")
		while  j < os.fstat(namafile.fileno()).st_size: # prevent EOF
			if namafiles[j] == "#" :
				if os.fstat(namafile.fileno()).st_size - j > 3 :
					pesanke += 1
					print ("\n",pesanke,". ",end="")
			else :
				print (namafiles[j],end='')
			j += 1
		namafiles.close
		namafile.close
	search.close

# add
def add():
	listfile = open(listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_WRITE)
	error = 0
	i = 0
	while search[i] != ":":
		i += 1	
	if len(sys.argv) == 2 : # amanat.py add
		print ("Display exists person:")
		j = i + 1
		while  j < os.fstat(listfile.fileno()).st_size: # prevent EOF
			if search[j] >= "a" and search[j] <= "z" or search[j] >= "A" and search[j] <= "Z" :
				print (search[j],end='')	
			j += 1
		search.seek(0)	
		nama = str(raw_input("\nchoose (or write new person): ")) # can make more than 1 word
		message = str(raw_input("Write the message\n\n"))
	elif len(sys.argv) == 3 : # amanat.py add name
		nama = str(sys.argv[2])
		message = str(raw_input("Write the message\n\n"))
	elif len(sys.argv) == 4 : # amanat.py add name "message"
		nama = str(sys.argv[2])
		message = str(sys.argv[3])
	else :
		print ("your argument is too much")
		error = 1

	if not error:
		try : 
			namafile = open(path + nama + ".txt", 'a+')
			if search.find(nama + " ") != -1 : # already exist
				j = i + 1
				lennama = len(nama) + 1
				while  j < os.fstat(listfile.fileno()).st_size-lennama:
					if search[j] == nama[0] :
						k = 0
						for x in range(0,lennama-1):
							if search[j+x] == nama[x] :
								k = 1
							else :
								k = 0
								break
						if k :
							break
					j += 1
				k = 0
				x = ""
				while search[j+lennama+k] != "#" :
					x = x + search[j+lennama+k]
					k += 1
				search[j+lennama:j+lennama+k] = str(int(x)+1)
			else :
				listfile.write(nama + " 1#\n")
			namafile.write(message + " #\n")
			namafile.close()
			print ("Success")
		except IOError, e:
			print ("failed : ", e)
	search.flush()
	search.close()
	listfile.close()
	return 0

# remove
def remove():
	print ("remove function")

# rename
def rename():
	print ("rename function")

# merge
def merge():
	print ("merge function")

# help
def help():
	print ("""
	Amanat - Save a message that trusted to you
	
	-- Synopsis
	
	$: amanat.py [Options]
	
	-- Options
	
	> random
	Default options. Display random message from random person.
	
	> view [all|name] [all|number of message]
	The first argument decide message from who will display. all is default. The second argument decide which message will display. all is default. Choose name or/and number of message to spesific display. Numbering was sorted ascending (oldest on top).
	
	> add [blank|name] ["message"]
	The first argument decide message from who will add. blank is default. If blank choosed, showing the list of person that already exist then asking for person. If you put person that not exist, will make a new person to list. Name of person just alphabetic without space. message must be in (double) quote.
	
	> remove [all|name] [all|number of message]
	The first argument decide message from who will remove. all is default. The second argument decide which message will remove. all is default. Choose name or/and number of message to spesific remove. Numbering was sorted ascending (oldest on top)
	
	> merge [all|name] [all|number of message] [all|name] [all|number of message] [merge name]
	You can merge 2 message from 2 person. Merge name is the merge message will be save. Old messege will be delete.
	
	> help 
	Display this help.
	
	> version
	Display version of amanat program
	
	> about
	Display about this program
	
		""")

# version
def version():
	print ("Amanat v0.01")

# check argument
if len(sys.argv) == 1 :
	random()
elif str(sys.argv[1]) == "random" :
	random()
elif str(sys.argv[1]) == "view" :
	view()
elif str(sys.argv[1]) == "add" :
	add()
elif str(sys.argv[1]) == "remove" :
	remove()
elif str(sys.argv[1]) == "rename" :
	rename()
elif str(sys.argv[1]) == "merge" :
	merge()
elif str(sys.argv[1]) == "help" :
	help()
elif str(sys.argv[1]) == "version" :
	version()
elif str(sys.argv[1]) == "about" :
	about.about()
else :
	print ("Wrong Options")