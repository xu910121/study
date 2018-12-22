#!/usr/bin/python3
#coding: utf-8

import re
from urllib import request, error
import urllib

class BDTB:

	def __init__(self,baseUrl,seelz):
		self.baseUrl = baseUrl
		self.seelz = '?see_lz=' + str(seelz)

	#传入页码，获取该页帖子的代码
	def getPage(self, pageNum):
		try:
			url = self.baseUrl + self.seelz + '&pn=' + str(pageNum)
			request = urllib.request.Request(url)
			response = urllib.request.urlopen(request)
			print(response.read().decode('utf-8'))
			return response
		except urllib.error.URLError as e:
			if hasattr(e, 'reason'):
				print(u'连接百度贴吧失败，错误原因：', e.reason)

baseUrl = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseUrl, 1)
bdtb.getPage(1)