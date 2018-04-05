#!/usr/bin/python

import base64
import codecs
import hashlib
import hmac

def level1Solution(data):
	h = hashlib.md5()
	h.update(data)
	return h.hexdigest()

def level2Solution(data):
	h = hashlib.sha256()
	for d in data:
		h.update(d)
	return h.hexdigest()

def level3Solution(data):
	return base64.b64encode(data)

def level4Solution(data):
	return base64.b16decode(data)

def level5Solution(data):
	key = "Ca3saR"
	h = hmac.new(key, data, hashlib.sha1)
	return h.hexdigest()

def level6Solution(data):
	return codecs.encode(data, 'rot_13')

solutions = [level1Solution,
	     level2Solution,
	     level3Solution,
	     level4Solution,
	     level5Solution,
	     level6Solution]
