#!/usr/bin/python

def level1Solution(data):
	return data.upper()

def level2Solution(data):
	return data.lower()

def level3Solution(data):
	return data.capitalize()

def level4Solution(data):
	return data.swapcase()

def level5Solution(data):
	return data.isalnum()

def level6Solution(data):
	return data.strip('A')

def level7Solution(data):
	return data.replace('A','Z')

def level8Solution(data):
	if "StringsRfun" in data:
		return 1
	else:
		return 0

def level9Solution(data):
	return data.rfind('StringsRfun')

def level10Solution(data):
	return data[2]

def level11Solution(data):
	return data[-2]

def level12Solution(data):
	return data[:10]

def level13Solution(data):
	return data[-9:]

def level14Solution(data):
	return data[2:9]

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution,
	     level7Solution,
	     level8Solution,
	     level9Solution,
	     level10Solution,
	     level11Solution,
	     level12Solution,
	     level13Solution,
	     level14Solution]