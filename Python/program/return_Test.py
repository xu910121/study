#!/usr/bin/python 

def test():
	print 'dhfg;ldsagf'
	for x in range(100):
		if x == 50:
			print "return"
			return 0

t = test()
if t == 0:
	exit()

print "can print ??"