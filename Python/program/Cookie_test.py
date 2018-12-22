#!/usr/bin/python3

from urllib import request, parse
from http import cookiejar

filename = 'cookie.txt'

cookie = cookiejar.MOzillaCookieJar(filename)
opener = request.build_opener(request.HTTPCookieProcessor(cookie))

postdata = parse.urlencode({
    'stuid':'12006310425'
    'pwd':''
})

loginUrl = 'http://'