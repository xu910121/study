#!/usr/bin/python3
#coding:utf-8

from urllib import request, error, parse
import urllib
import re

page = 1
while True:
	global page
	print('page = %d' % page)
	url = 'http://www.qiushibaike.com/hot/page/' + str(page)
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5,5;Windows NT)'
	headers = {'User-Agent': user_agent}
	try:
		request = urllib.request.Request(url, headers = headers)
		response = urllib.request.urlopen(request)
	except error.URLError as e:
		if hasattr(e, 'code'):
			print(e.code)
		if hasattr(e, 'reason'):
			print(e.reason)

	content = response.read().decode('utf-8')
	pattern = re.compile('<div.*?>.*?<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?href(.*?)</li>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		if 'img src' not in item[2]:
			with open(r'div.txt','a+',encoding='utf-8') as f:
				res = '作者：' + item[0] + '\n' + '内容：' + item[1] + '\n'
				f.write(res)
		#print('作者：%s\n内容：%s\n' % (item[0],item[1]))
		#print(item[2])
	page +=1
	if page >35:
		break