# -*- coding: cp936 -*-
#file:tcpserver.py

import socket
from time import ctime
import sys

bufsize = 1024
host = '127.0.0.1'
port = 8100
address = (host,port)

server_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_sock.bind(address)
server_sock.listen(1)

while True:
    print 'waiting for connection...'
    clientsock,addr = server_sock.accept()
    print 'received from :',addr

    while True:
        data = clientsock.recv(bufsize)
        print ' �յ�---->%s\n%s' %(ctime(),data)
        data = raw_input("����----->")
        clientsock.send(data)
    clientsock.close()

server_sock.close()