#!/usr/bin/python

import re, fileinput

f = open('e:\grub.cfg','r+')
m = re.compile(r"^menuentry '\xe4\xb8\xad\xe7\xa7\x91\xe6\x96\xb9\xe5\xbe\xb7")
for line in f:
	s = m.search(line)
	if s:
		line = line.split()
		del line[3]
		line.insert(3,'GE-6123215614_test-ZBR-01')
		line = ' '.join(line)
		f.write(line)