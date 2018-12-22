#!/usr/bin/python
import urllib2
import re
import commands.getoutput

url = "http://www.vladstudio.com/en/wallpaperclocks/browse.php?skip=0"
result = urllib2.urlopen(url).read()
source = re.compile(r'<a href="(http://www.vladstudio.com/wallpaperclock/\?\w*)">')
down = re.compile(r'http://files.vladstudio.com/joy/\w+/wcz/vladstudio_\w+_1920x1080.wcz')
items = re.findall(source, result)
for item in items:
	print item
	r = urllib2.urlopen(item).read()
	arrs = re.findall(down,r)
	for arr in arrs:
		commands.getoutput("wget -P /home/dange/dexclock" +  arr)