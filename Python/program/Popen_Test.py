#!/usr/bin/python
#coding:utf-8

import subprocess

#����Popen�Ƿ�Ϊ���������Խ����ʾΪ��������
cmd = "ping -c 5 www.google.com"
#child = subprocess.Popen(cmd,stdout=subprocess.STDOUT)
print("parent process")

cmd = 'dir'
c = subprocess.Popen(cmd,stdout=subprocess.PIPE)
print c.communicate()