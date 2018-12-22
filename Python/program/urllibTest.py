import urllib2

url = r'http://www.baidu.com'
req = urllib2.Request(url)
html = urllib2.urlopen(req).read()

f = open(r'E:\html','w+')
f.write(html)
f.close()