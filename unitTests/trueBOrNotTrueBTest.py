#!/usr/bin/python

def level1Solution(data):
	return True

def level2Solution(data):
	return False

def level3Solution(data):
	return data < 1500

def level4Solution(data):
	return data <= 1500

def level5Solution(data):
	return data > 1500

def level6Solution(data):
	return data >= 1500

def level7Solution(data):
	return data == 1500

def level8Solution(data):
	return data != 1500

def level9Solution(data):
	return data or False

def level10Solution(data):
	return data and True

def level11Solution(data):
	return not data

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
	     level11Solution]
