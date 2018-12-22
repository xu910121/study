#!/usr/bin/python
#conding:utf-8
#使用分叉技术的服务器。
#因为windows不支持分叉，所以这个不能在windows上运行。

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):pass

class Handler(StreamRequestHandler):

	def handle(self):
		add = self.request.getpeername()
		print "Got connect from", addr
		self.wfile.write("Thank you from connecting")

server = Server(('',1234), Handler)
server.serve_forever()