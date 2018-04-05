#!/usr/bin/python

def level1Solution(data):
	return data + 1024

def level2Solution(data):
	return data - 1024

def level3Solution(data):
	return data * 1024

def level4Solution(data):
	return data / 1024

def level5Solution(data):
	return data % 1024

def level6Solution(data):
	return -data

def level7Solution(data):
	return abs(data)

def level8Solution(data):
	return pow(data, 2)

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution,
	     level7Solution,
	     level8Solution]