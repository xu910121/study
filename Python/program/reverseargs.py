#!/usr/bin/python
#coding:utf-8

import sys
if len(sys.argv) < 2:
	print '����������в���'
	sys.exit(1)
args = sys.argv[1:]
args.reverse()
print args