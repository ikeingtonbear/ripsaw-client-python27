#!/usr/bin/python

"""RIPSAW Client Library - Python 2.7
The RIPSAW Client Library is used to interact with the RIPSAW server."""

import re, socket

from ripsawClient import xmlLib

class Game:
	"""The Game class is the object used to interact with RIPSAW games
	hosted on the RIPSAW server.  Some RIPSAW games are password
	protected, and therefore a correct password is needed in order to
	access the game. The idea of a RIPSAW game is that there are
	challenges which need to be solved. Each challenge has data which
	needs to be manipulated and submitted as an answer in order to
	solve the challenge. At the end of the game a flag is returned."""

	def __init__(self):
		"""Setup initial values needed for the RIPSAW game"""
		self.serverIP = None
		self.serverPort = None
		self.sessionSocket = None
		self.requestFactory = xmlLib.RequestFactory()
		self.responseHandler = xmlLib.ResponseHandler()

	def connect(self):
		"""Connect to the RIPSAW game server"""

		if not self.serverIP and not self.serverPort:
			print("Could not connect to server. No IP address and port specified")
			return
		elif not self.serverIP:
			print("Could not connect to server. No IP address specified")
			return
		elif not self.serverPort:
			print("Could not connect to server. No port specified")
			return
		try:
			self.sessionSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.sessionSocket.connect((self.serverIP, self.serverPort))
		except:
			print("Could not establiblish a connection to the server")
		try:
			bannerXML = self.sessionSocket.recv(1024).strip().decode('utf-8')
			print self.responseHandler.handle(bannerXML)

		except:
			print("Unable to grab banner")

	def disconnect(self):
		"""Disconnect from the RIPSAW game server"""
		try:
			self.sessionSocket.sendall('\n')
			self.sessionSocket.close()
		except:
			print("Unable to disconnect")

	def setServerIP(self, ipAddr):
		"""Set the IP address of the RIPSAW game server"""
		IPREGEX="^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
		if re.match(IPREGEX, ipAddr):
			self.serverIP=ipAddr
		else:
			print("{} is an invalid IP Address".format(ipAddr))

	def getServerIP(self):
		"""View the IP address that is currently set"""
		if self.serverIP:
			return self.serverIP
		else:
			print("Server IP Address has not been set")

	def setServerPort(self, port):
		"""Set the port that the RIPSAW game is served on"""
		if 1 <= port and port <=65535:
			self.serverPort=port
		else:
			print("Port {} is an invalid port".format(port))

	def getServerPort(self):
		"""View the port that is currently set"""
		if self.serverPort:
			return self.serverPort
		else:
			print("Server port has not been set")

	def setServer(self, ipAddr, port):
		"""Set the IP addres and port that the RIPSAW game is served on"""
		self.setServerIP(ipAddr)
		self.setServerPort(port)

	def getServer(self):
		"""View the IP addres and port that are currently set"""
		return self.serverIP,self.serverPort

	def password(self, password):
		"""Send a password to gain access to the RIPSAW game"""
		passwordXML = self.requestFactory.generatePassword(password)
		self.sessionSocket.sendall(passwordXML)
		xmlString = self.sessionSocket.recv(1024).strip().decode('utf-8')
		print self.responseHandler.handle(xmlString)

	def getChallenge(self):
		"""Request the current challenge/problem statement from the RIPSAW game"""
		challengeXML = self.requestFactory.generateQuestion()
		self.sessionSocket.sendall(challengeXML)
		xmlString = self.sessionSocket.recv(1024).strip().decode('utf-8')
		print self.responseHandler.handle(xmlString)

	def getData(self):
		"""Request the current data from the RIPSAW game"""
		dataXML = self.requestFactory.generateData()
		self.sessionSocket.sendall(dataXML)
		xmlString = self.sessionSocket.recv(1024).strip().decode('utf-8')
		return self.responseHandler.handle(xmlString)

	def submitAnswer(self, answer):
		"""Submit the answer to the current challenge"""
		answerXML = self.requestFactory.generateAnswer(answer)
		self.sessionSocket.sendall(answerXML)
		xmlString = self.sessionSocket.recv(1024).strip().decode('utf-8')
		print self.responseHandler.handle(xmlString)
