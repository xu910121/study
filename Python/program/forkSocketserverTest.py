#!/usr/bin/python
#conding:utf-8
#ʹ�÷ֲ漼���ķ�������
#��Ϊwindows��֧�ֲַ棬�������������windows�����С�

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):pass

class Handler(StreamRequestHandler):

	def handle(self):
		add = self.request.getpeername()
		print "Got connect from", addr
		self.wfile.write("Thank you from connecting")

server = Server(('',1234), Handler)
server.serve_forever()