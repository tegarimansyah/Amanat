from __future__ import print_function
import mmap
import os
import _config

def data(argv) :
	listfile = open(_config.listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_READ)
	error = 0
	i = 0
	while search[i] != ":":
		i += 1	
	if len(argv) == 2 : # amanat.py view
		print ("Display exists person:")
		j = i + 1
		while  j < os.fstat(listfile.fileno()).st_size: # prevent EOF
			if search[j] >= "a" and search[j] <= "z" or search[j] >= "A" and search[j] <= "Z" :
				print (search[j],end='')				
			j += 1
		search.seek(0)	
		nama = str(raw_input("\nchoose person: ")) # can make more than 1 word
		# number = int(raw_input("Write the message: "))
	elif len(argv) == 3 : # amanat.py view name
		nama = str(argv[2])
		# message = str(raw_input("Write the message\n\n"))
	elif len(argv) == 4 : # amanat.py view name number
		nama = str(argv[2])
		# message = str(argv[3])
	else :
		print ("your argument is too much")
		error = 1

	if not error and os.path.exists(_config.path + nama + ".txt"):
		namafile = open(_config.path + nama + ".txt", 'a+')
		# Old algorithm
		# namafiles = mmap.mmap(namafile.fileno(), 0, access=mmap.ACCESS_READ)
		# j = 0
		# pesanke = 1
		# print(nama," said that :\n\n",pesanke,". ",end="")
		# while  j < os.fstat(namafile.fileno()).st_size: # prevent EOF
		# 	if namafiles[j] == "#" :
		# 		if os.fstat(namafile.fileno()).st_size - j > 3 :
		# 			pesanke += 1
		# 			print ("\n",pesanke,". ",end=''),
		# 	else :
		# 		print (namafiles[j].rstrip("\n"),end='')
		# 	j += 1
		# print ("\n")
		# namafiles.close
		pesanke = 1
		for line in namafile :
			print (pesanke,".", line.strip().strip('#'))
			pesanke += 1
		namafile.close
	search.close