#!/usr/bin/python

from sys import exit

import ripsaw
from unitTests import backToTheAbacusTest
from unitTests import trueBOrNotTrueBTest
from unitTests import decisionsDecisionsTest
from unitTests import stringTheoryTest
from unitTests import listsOnListsOnListsTest
from unitTests import secondIterationTest
from unitTests import justABitLoopyTest
from unitTests import merriamWebstersUrbanTest
from unitTests import hashtagCryptoTest


game = ripsaw.Game()
game.setServerIP('127.0.0.1')

print "Testing backToTheAbacus"
game.setServerPort(8003)
game.connect()
try:
	game.password('2PiRskwar3d')
except:
	exit("PASSWORD: 8003")
for lvl in backToTheAbacusTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing trueBOrNotTrueB"
game.setServerPort(8004)
game.connect()
game.password('bool3an_L0gic')
for lvl in trueBOrNotTrueBTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing decisionsDecisions"
game.setServerPort(8005)
game.connect()
game.password('if3ls33ndif')
for lvl in decisionsDecisionsTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing stringTheory"
game.setServerPort(8006)
game.connect()
game.password('bran3sandDbran3s')
for lvl in stringTheoryTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing listsOnListsOnLists"
game.setServerPort(8007)
game.connect()
game.password('Ind!c3sRK3y')
for lvl in listsOnListsOnListsTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing secondIteration"
game.setServerPort(8008)
game.connect()
game.password('It3r2t@k3Tw0')
for lvl in secondIterationTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing justABitLoopy"
game.setServerPort(8009)
game.connect()
game.password('T0ucan$am')
for lvl in justABitLoopyTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing merriamWebstersUrban"
game.setServerPort(8010)
game.connect()
game.password('Urb@nD0tC0m')
for lvl in merriamWebstersUrbanTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()

print "Testing hashtagCrypto"
game.setServerPort(8011)
game.connect()
game.password('3ni9maM@ch!n3')
for lvl in hashtagCryptoTest.solutions:
	try:
		game.getChallenge()
	except:
		exit("getChallenge"+str(lvl))

	try:
		data = game.getData()
	except:
		exit("getData"+str(lvl))

	try:
		game.submitAnswer(lvl(data))

	except:
		exit("submitAnswer"+str(lvl))
game.disconnect()
	
