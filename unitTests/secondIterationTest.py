#!/usr/bin/python

def level1Solution(data):
	return len(data)

def level2Solution(data):
	return len(data)

def level3Solution(data):
	return sum(data)

def level4Solution(data):
	return "HelloWorld" in data

def level5Solution(data):
	return "HelloWorld" not in data

def level6Solution(data):
	return data.split()

def level7Solution(data):
	return data.split('/')

def level8Solution(data):
	return "".join(data)

def level9Solution(data):
	return ".".join(data)

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution,
	     level7Solution,
	     level8Solution,
	     level9Solution]