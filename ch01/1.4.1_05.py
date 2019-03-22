# coding:utf-8

# 5.pipe进程间通信

import multiprocessing
import os
import random
import time


def proc_send(pipe, urls):
    for url in urls:
        print "Process(%s) send: %s" % (os.getpid(), url)
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print "Process(%s) rev:%s" % (os.getpid(), pipe.recv())
        time.sleep(random.random())
