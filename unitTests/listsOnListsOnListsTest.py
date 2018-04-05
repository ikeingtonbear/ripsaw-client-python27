#!/usr/bin/python

def level01Solution(data):
	return data[0]

def level02Solution(data):
	return data[-1]

def level03Solution(data):
	return data[4]

def level04Solution(data):
	return data[:3]

def level05Solution(data):
	return data[-3:]

def level06Solution(data):
	return data[3:-3]

def level07Solution(data):
	c = data
	c[3] = "HelloWorld"
	return c

def level08Solution(data):
	return data.insert(3, 'HelloWorld')

def level09Solution(data):
	return data.append('HelloWorld')

def level10Solution(data):
	print data
	return data.remove("HelloWorld")

def level11Solution(data):
	return data.reverse()

def level12Solution(data):
	return data.sort()

def level13Solution(data):
	return data[0].extend(data[1])

solutions = [level01Solution,
	     level02Solution,
	     level03Solution,
	     level04Solution,
	     level05Solution,
	     level06Solution,
	     level07Solution,
	     level08Solution,
	     level09Solution,
	     level10Solution,
	     level11Solution,
	     level12Solution,
	     level13Solution]