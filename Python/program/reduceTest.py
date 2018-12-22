#!/usr/bin/python
#coding: utf-8
#reduce()ÄÚ½¨º¯Êı²âÊÔ¡£

m = []
for i in range(10):
	m.append(set(range(i,i+5)))

print 'm =', m
print 'reduce(set.union,m) =', reduce(set.union, m)