#!usr/bin/python
# -*- coding: utf-8 -*-

class Operaciones(object):
	"""docstring for ClassName"""
	def __init__(self, num1, num2):
		self.num1 = num1
		self.num2 = num2

	def suma(self):
		return self.num1+self.num2

	def resta(self):
		return self.num1-self.num2	

obj = Operaciones(3, 7)
print obj.suma()
print obj.resta()

		