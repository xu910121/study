#!/usr/bin/python
#try:
#	x = input("Enter the first number:")
#	y = input("Enter the second number:")
#	print x/y
#except (ZeroDivisionError), e:
#	print e

def describePerson(person,*test):
	print 'Description of', person['name']
	print 'Age:', person['Age']
	print test
	if 'occupation' in person:
		print 'Occupation:', person['occupation']

person = {'name':'Thtoatwobbler', 'Age':42}
describePerson(person,1)

def test(**args):
	print args

test(1, 2, 3)