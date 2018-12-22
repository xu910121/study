#!/usr/bin/python

from string import maketrans,translate
test = maketrans('zg', 'cs')
print test
str = "zhangdongxuaizuguo"
result = translate(str, test)
print result