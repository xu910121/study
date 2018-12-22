#!/usr/bin/python
#coding: utf-8

def yieldTest(num):
	for x in num:
		yield x

for x in yieldTest((1,2,3)):
	print x

y = yieldTest([1])
print 'y.next() =', y.next()
y.send([1,2])
#print y.next()

#µÝ¹éÉú³ÉÆ÷£º
def flatten(nested):
	try:
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested

for x in flatten([[1,[2,3,[4,5]]],6,7,[8,[9,10]]]):
	print x


def repeater(value):
	while True:
		new = (yield value)
		if new is not None:
			value = new

r = repeater(42)
print 'r.next() =', r.next()
print "r.send('Hello, World!') = ", r.send("Hello, World!")
print "r.next() = ", r.next()
r.close()
print "r.next() = ", r.next()