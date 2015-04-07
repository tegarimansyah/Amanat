from __future__ import print_function
import mmap
import os
import _config

def new(argv) :
	listfile = open(_config.listpath, 'a+')
	search = mmap.mmap(listfile.fileno(), 0, access=mmap.ACCESS_WRITE)
	error = 0
	i = 0
	while search[i] != ":":
		i += 1	
	if len(argv) == 2 : # amanat.py add
		print ("Display exists person:")
		j = i + 1
		while  j < os.fstat(listfile.fileno()).st_size: # prevent EOF
			if search[j] != " " and not (search[j] >= "0" and search[j] <= "9") and search[j] != "#":
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

	nama = nama.lower()
	if not error:
		try : 
			namafile = open(_config.path + nama + ".txt", 'a+')
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
				print (int(x))
				if int(x) == 9 :
					search[j+lennama:j+lennama+log(int(x),3)] = str(int(x)+1) + "#"
				else :
					search[j+lennama:j+lennama+k] = str(int(x)+1)
			else :
				listfile.write(nama + " 1#\n")
				i = 0
				z = 0
				numb = ""
				while search[z] != " " :
					numb = numb + search[z]
					z += 1
				search[0:z] = str(int(numb)+1)
			namafile.write(message + " #\n")
			namafile.close()
			print ("Success")
		except IOError, e:
			print ("failed : ", e)
	search.flush()
	search.close()
	listfile.close()

# def newest(x):
# 	print (x)
# 	if int(x) % 10 == 0 :
# 		return newest(int(x)/10)
# 	elif int(x) == 1 :
# 		return 1
# 	else :
# 		return 0

# def log(x,i) :

# 	if x / 10 >=10 :
# 		i += 1
# 		return log(x/10,i)
# 	else :
# 		return i
