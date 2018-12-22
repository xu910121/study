#!/usr/bin/python
#coding: utf-8
#测试类变量与实例变量
class test:
	name = 'test'
	val = 5
	sum = 0

	def __init__(self, val, sum):
		self.val = val + 10
		self.sum = sum + 100
	
	def te(self):
		print self.val
		print self.sum
		print self.name

T = test(1, 5)
T.te()
print test.sum