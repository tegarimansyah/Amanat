from __future__ import print_function
import mmap
import os
import config
import random

#random
def rando():

	# Searching for numb
	listfile = open(config.listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_READ)
	i = 0
	numb = ""
	while search[i] != " " :
		numb = numb + search[i]
		i += 1
	numb = int(numb)
	numb = random.randint(1,numb)
	while search[i] != ":":
		i += 1	

	# Searching for name
	personke = 1
	person = ""
	while  i < os.fstat(listfile.fileno()).st_size: # prevent EOF
		if int(personke) == numb and (search[i] >= "a" and search[i] <= "z" or search[i] >= "A" and search[i] <= "Z" ):
			while search[i] != " " :
				person = person + search[i]
				i += 1
			break

		if search[i] == "#" :
			personke += 1
		i += 1
	print ("(random message)",person,"said that: ",end="")
	
	# Searching numb of amanat
	numb = ""
	while  i < os.fstat(listfile.fileno()).st_size: # prevent EOF
		if search[i] >= "0" and search[i] <= "9" :
			numb = numb + search[i]
		if search[i] == "#" :
			break
		i += 1
	numb = int(numb)
	numb = random.randint(1,numb)
	search.close
	listfile.close

	# Searching for amanat
	listfile = open(config.path + person + ".txt", 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_READ)
	amanatke = 1
	i = 0
	while  i < os.fstat(listfile.fileno()).st_size: # prevent EOF
		if int(amanatke) == numb and (search[i] >= "a" and search[i] <= "z" or search[i] >= "A" and search[i] <= "Z" ):
			while search[i] != "#" :
				print (search[i],end='')
				i += 1
			break

		if search[i] == "#" :
			amanatke += 1
		i += 1
	print ("\n")