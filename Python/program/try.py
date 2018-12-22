#!/usr/bin/python

try:
	1/1
except TabError:
	print "over"
else:
	print 'no'
finally:
	print 'gg'