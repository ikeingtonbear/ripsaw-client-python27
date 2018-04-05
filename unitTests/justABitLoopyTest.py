#!/usr/bin/python

def level1Solution(data):
	total = 0
	for i in range(data):
		total+=i
	return total

def level2Solution(data):
	total = 0
	for i in range(data[0], data[1]):
		total+=i
	return total

def level3Solution(data):
	total = 0
	for i in range(data[0], data[1],2):
		total+=i
	return total

def level4Solution(data):
	caps = []
	for s in data:
		caps.append(s.upper())
	return caps

def level5Solution(data):
	ans = []
	for i in data:
		ans.append(i+20)
	return ans

def level6Solution(data):
	ans = []
	for i, j in data:
		ans.append(j-i)
	return ans

def level7Solution(data):
	ans = []
	for i, j in data:
		ans.append("".join([j,i]))
	return ans

def level8Solution(data):
	ans = []
	for i in data:
		for j in i:
			ans.append(j.lower())
	return ans

def level9Solution(data):
	data2 = data[:-1]
	diff = data[-1]
	for i in reversed(data2):
		diff-=i
	return diff

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution,
	     level7Solution,
	     level8Solution,
	     level9Solution]