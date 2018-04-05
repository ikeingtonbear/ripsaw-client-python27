#!/usr/bin/python

def level1Solution(data):
	return len(data)

def level2Solution(data):
	return list(data.keys()).sort()

def level3Solution(data):
	return list(data.values()).sort()

def level4Solution(data):
	return 'HelloWorld' in data

def level5Solution(data):
	return data['HelloWorld']

def level6Solution(data):
	data2 = data
	data2['Hello'] = 'World'
	return data2

def level7Solution(data):
	a,b = data
	return a.update(b)

def level8Solution(data):
	tempData = data
	for k,v in tempData.iteritems():
		tempData[k] = v+20
	return tempData

def level9Solution(data):
	tempData = data
	for k,v in tempData.iteritems():
		tempData[k] = 'HelloWorld'
	return tempData

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution,
	     level7Solution,
	     level8Solution,
	     level9Solution]