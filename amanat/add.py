from __future__ import print_function
import mmap
import os
import config

def new(argv) :
	listfile = open(config.listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_WRITE)
	error = 0
	i = 0
	while search[i] != ":":
		i += 1	
	if len(argv) == 2 : # amanat.py add
		print ("Display exists person:")
		j = i + 1
		while  j < os.fstat(listfile.fileno()).st_size: # prevent EOF
			if search[j] >= "a" and search[j] <= "z" or search[j] >= "A" and search[j] <= "Z" :
				print (search[j],end='')	
			j += 1
		search.seek(0)	
		nama = str(raw_input("\nchoose (or write new person): ")) # can make more than 1 word
		message = str(raw_input("Write the message\n\n"))
	elif len(argv) == 3 : # amanat.py add name
		nama = str(argv[2])
		message = str(raw_input("Write the message\n\n"))
	elif len(argv) == 4 : # amanat.py add name "message"
		nama = str(argv[2])
		message = str(argv[3])
	else :
		print ("your argument is too much")
		error = 1

	if not error:
		try : 
			namafile = open(config.path + nama + ".txt", 'a+')
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