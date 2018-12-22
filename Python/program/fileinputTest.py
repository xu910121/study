#!/usr/bin/python                                                      #  1
#coding:utf-8                                                          #  2
__metaclass__ = type                                                   #  3
                                                                       #  4
import fileinput                                                       #  5
import sys                                                             #  6
                                                                       #  7
if len(sys.argv) < 2 :                                                 #  8
    print "没有要处理的文件"                                           #  9
else:                                                                  # 10
    for line in fileinput.input():                                     # 11
        print line                                                     # 12
                                                                       # 13
if len(sys.argv) >= 2 :                                                # 14
    pass                                                               # 15
    #print "处理了fileinput.lineno() = %d行" % fileinput.lineno()      # 16
                                                                       # 17
#for x in fileinput.input():                                           # 18
#   print x                                                            # 19
#   print fileinput.isstdin()                                          # 20
                                                                       # 21
for line in fileinput.input(inplace=True,backup='.bak'):               # 22
    line = line.rstrip()                                               # 23
    num = fileinput.lineno()                                           # 24
    line = line.expandtabs(4)                                          # 25
    print '%-70s # %2i' % (line,num)                                   # 26