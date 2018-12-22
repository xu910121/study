#!/usr/bin/python
#coding:utf-8


class Test:
	def __init__(self):
		print "This is a __name__ and class run test"
		print_t()
		say_t()

class T:
	@staticmethod
	def print_t():
		print "aha, Who are you?", __name__
	
	@staticmethod
	def say_t():
		print 'Hello, World!'

if __name__ == '__main__':
	T.print_t()
	T.say_t()