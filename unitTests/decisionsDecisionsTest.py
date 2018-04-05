#!/usr/bin/python

def level1Solution(data):
	if data:
		return 1
	else:
		return 0

def level2Solution(data):
	if data:
		return 1
	else:
		return 0

def level3Solution(data):
	if data>1024:
		return 1
	elif data == 1024:
		return 0
	else:
		return -1

def level4Solution(data):
	if data>1250 and data <1750:
		return 1
	else:
		return 0

def level5Solution(data):
	if data<1250 or data>1750:
		return 1
	else:
		return 0

def level6Solution(data):
	if data<1250 or data>1750:
		return 1
	elif data>1400 and data<1500:
		return 0
	else:
		return -1
	
solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution]