#!/usr/bin/python
#coding: utf-8
#from _future_ import division 似乎不用了？
print 1/2
print "hello" "world"
print ('% 5d' % 10) + '\n' + ('% 5d' % -10)

t = 1
#assert t > 2			#断言

a = [1, 2, 3, 4, 5]		#测试editplus是否会自动缩进
b = 1
if b in a:
	print "OK"
print "END"

s = ['t', 'x', 'w', 'd']
for index, string in enumerate(s):
	print index, string

from math import sqrt
print sqrt(4)

if s:
	pass