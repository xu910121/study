#!/usr/bin/python
#coding:utf-8

import sys
if len(sys.argv) < 2:
	print '请带上命令行参数'
	sys.exit(1)
args = sys.argv[1:]
args.reverse()
print args