#!/usr/bin/python
#coding:utf-8

import subprocess

#测试Popen是否为阻塞。测试结果显示为非阻塞。
cmd = "ping -c 5 www.google.com"
#child = subprocess.Popen(cmd,stdout=subprocess.STDOUT)
print("parent process")

cmd = 'dir'
c = subprocess.Popen(cmd,stdout=subprocess.PIPE)
print c.communicate()