#!/usr/bin/python
#coding:utf-8
#使用select完成的简单服务器

import select, socket

S = socket.socket()

host = socket.gethostname()
port = 1234
S.bind ((host,port))

S.listen(5)
inputs = [S]
while True:
	rs, ws, es = select.select(inputs, [], [])
	for r in rs:
		if r is S:
			c, addr = S.accept()
			print "Got connection from", addr
			inputs.append(c)
		else:
			try:
				data = r.recv(1024)
				print data
				r.send("Ni,Hao")
				disconnected = not data
			except socket.error:
				disconnected = True

				if disconnected:
					print r.getpeername(), 'disconnected'
					inputs.remove(r)
				else:
					print data