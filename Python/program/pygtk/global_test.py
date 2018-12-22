#!/usr/bin/python

import threading
import time

class T1(threading.Thread):
    global name
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        name = "T1"
        print "T1"

class T2(threading.Thread):
    global name
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        print "T2 : name = %s" % name
        time.sleep(1)

global name
name = "Main"


while(True):
    print "Main : name = %s" % name
    t1 = T1()
    t2 = T2()
    t1.start()
    t2.start()
    time.sleep(1)
