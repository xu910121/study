## -*- coding: cp936 -*-
##file��tcpclient.py

from socket import *
from time import ctime

bufsize = 1024
host = '127.0.0.1'
port = 8100
addr = (host,port)

client_sock = socket(AF_INET,SOCK_STREAM)
client_sock.connect(addr)

while True:
    data = raw_input("����---->")
    if not data:
        break
    else:
        client_sock.send(data)
        data = client_sock.recv(bufsize)
        print '�յ�---->%s\n%s' %(ctime(),data)

client_sock.close()