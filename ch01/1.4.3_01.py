# coding:utf-8

# 1.gevent的使用流程

import urllib2

import gevent
from gevent import monkey

monkey.patch_all()


def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception, e:
        print e


if __name__ == '__main__':
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    GreenLets = [gevent.spawn(run_task, url) for url in urls]
    gevent.joinall(GreenLets)

'''
Visit --> https://github.com/
Visit --> https://www.python.org/
Visit --> http://www.cnblogs.com/
47559 bytes received from http://www.cnblogs.com/.
48595 bytes received from https://www.python.org/.
82559 bytes received from https://github.com/.
'''