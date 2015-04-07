#!/bin/usr/env python
import shlex

def something() :
	inp = raw_input()
	inp = shlex.split(inp)
	i = -1
	global argv
	argv = []
	while i < len(inp):
		if i == -1 :
			argv.append("amanat.py")
		else :
			argv.append(inp[i])
		i += 1
	

def argv():
	return argv