#!/bin/python
#coding: utf-8
__metaclass__ = type
class Filter:
	#name = ''
	def init(self):
		self.blocked = []
		self.test = 'b'  ###################
	def filter(self,sequence):
		test = 'a'  #################
		return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter):
	def init(self):
		self.blocked = ['SPAM']

f = Filter()
#print f.test   ERROR
f.init()
print 'init() test:' + f.test
print f.filter([1, 2, 3])
print "filter() test:" + f.test
try:
	f.init
	print "OKOKOKOKOKOKOKOKOKOKOK"
except:
	print "HHHHHHHHHHHH"

s = SPAMFilter()
s.init()
print s.filter(['SPAM', 'SPAM', 'SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM'])

print "��SPAMFilter��Filter�������𣿣�" 
if issubclass(SPAMFilter, Filter):
	print "��" 
else:
	print "����"

print Filter

print isinstance(s, SPAMFilter)
print isinstance(s, Filter)

print getattr(s, 'init', None)
print getattr(s, 'name', 'dange')

######################################################################################################################################################
class Rectangle:
	def __init__(self):
		self.width = 0
		self.height = 0
	def setSize(self,size):
		self.width, self.height = size   #�˴�Ĭ��size������Ԫ��������У����ұ���������Ԫ�ء���C���Բ�ͬ��������������ֵ
										 #c���Կ������� int a, b = 1������Python������a, b = 1, 2
	def getSize(self):
		return self.width, self.height
	size = property(getSize, setSize)
#	size = property()
#	size = property(getSize)
#	size = property(setSize)
r = Rectangle()
#r.size = 50, 60
print 'r.width = ' , r.width
print 'r.height = ' , r.height
print 'r.getSize = ' , r.getSize()
try:
	print 'r.size = ', r.size
except :
	print 'AttributeError: unreadable attribute'
r.setSize([150,100])
print "r.width = %d, r.heiht = %d" % (r.width,  r.height)
print '*******************************************'
try:
	r.size = 50, 60
except:
	raise
	print "Error "
print "r.width = %d, r.heiht = %d" % (r.width,  r.height)
#print "r.width = %d, r.heiht = %d" % r.size
print '*******************************************'
######################################################################################################################################################
print
print '######################################################################'
class MyClass:
	@staticmethod
	def smeth():
		print 'This is a static method'
	@classmethod
	def cmeth(cls):
		print 'This is a class method of' , cls

MyClass.smeth()
MyClass.cmeth()
m = MyClass()
m.smeth()
m.cmeth()
print '######################################################################'