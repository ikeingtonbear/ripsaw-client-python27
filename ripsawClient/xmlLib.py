#!/usr/bin/python

"""xmlLib - Python 2.7
The RIPSAW client XML parser used create responses and generate requests to
interact with the RIPSAW server."""

import xml.etree.ElementTree as ET
import json

questionType = "question"
dataType = "data"
answerType = "answer"
passwordType = "password"

class ResponseHandler:
	"""The ResponseHandler class is responsible for parsing the responses
	received from the RIPSAW server and returning the data to the RIPSAW client"""

	def handleQuestion(self, root):
		"""Parses the XML containing the question text from the RIPSAW server"""
		jsonQuestionText = root.findtext("questionText").decode('utf-8')
		questionText = json.loads(jsonQuestionText)
		return questionText

	def handleData(self, root):
		"""Parses the XML containing data from the RIPSAW server"""
		jsonData = root.findtext("data").decode('utf-8')
		data = json.loads(jsonData)
		return data

	def handleAnswer(self, root):
		"""Parses the XML containing the response to an answer submission from the RIPSAW server"""
		jsonAnswer = root.findtext("answer").decode('utf-8')
		answer = json.loads(jsonAnswer)
		return answer

	def handlePassword(self, root):
		"""Parses the XML containing the response to a password submission from the RIPSAW server"""
		jsonPassword = root.findtext("password").decode('utf-8')
		password = json.loads(jsonPassword)
		return password

	responseTypes = {questionType:handleQuestion, dataType:handleData, answerType:handleAnswer, passwordType:handlePassword}

	def handle(self, xmlString):
		"""Method to handle the parsing of XML responses from the RIPSAW server"""
		xmlRoot = ET.fromstring(xmlString)
		responseType = xmlRoot.get("classtype")
		return self.responseTypes.get(responseType)(self, xmlRoot)

class RequestFactory:
	"""The RequestFactory class is responsible for taking data from the RIPSAW
	client and generating all the requests which will be sent to the RIPSAW server"""

	xmlTypes = {questionType:"question", dataType:"data", answerType:"answer", passwordType: "password"}

	def generateBase(self, XMLTYPE):
		"""Creates the basic XML data structure for RIPSAW client requests"""
		baseXML = ET.Element("RIPSAW", classtype=XMLTYPE)
		return baseXML

	def generateQuestion(self):
		"""Creates the XML data structure to request the question text from the RIPSAW server"""
		baseXML = self.generateBase(self.xmlTypes.get(questionType))
		return ET.tostring(baseXML)

	def generateData(self):
		"""Creates the XML data structure to request data from the RIPSAW server"""
		baseXML = self.generateBase(self.xmlTypes.get(dataType))
		return ET.tostring(baseXML)

	def generateAnswer(self, answer):
		"""Creates the XML data structure to submit an answer to the RIPSAW server"""
		baseXML = self.generateBase(self.xmlTypes.get(answerType))
		answerXML = ET.SubElement(baseXML, "answer")
		answerXML.text = json.dumps(answer)
		return ET.tostring(baseXML)

	def generatePassword(self, password):
		"""Creates the XML data structure to submit a password to the RIPSAW server"""
		baseXML = self.generateBase(self.xmlTypes.get(passwordType))
		passwordXML = ET.SubElement(baseXML, "password")
		passwordXML.text = json.dumps(password)
		return ET.tostring(baseXML)
