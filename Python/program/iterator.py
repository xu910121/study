#!/usr/bin/python
#coding: utf-8
print '########################################################'
#斐波那契
class Fibs:
	def __init__(self):
		self.a = 0
		self.b = 1
	def next(self):
		self.a, self.b = self.b, self.a + self.b
		if self.a > 100000:
			raise StopIteration
		return self.a
	def __iter__(self):
		return self
fibs = Fibs()
print fibs
for f in fibs:
	if f > 1000:
		print f
		break
print 'fibs.next() =', fibs.next()
f = Fibs()
print list(f)   #使用迭代器得到序列。
print '########################################################'