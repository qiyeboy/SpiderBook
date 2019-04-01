# coding:utf-8

# 2.gevent pool对象使用

import urllib2

from gevent import monkey
from gevent.pool import Pool

monkey.patch_all()


def run_task(url):
    print 'Visit --> %s' % url
    try:
        response = urllib2.urlopen(url)
        data = response.read()
        print '%d bytes received from %s.' % (len(data), url)
    except Exception, e:
        print e
    return 'url:%s --->finish' % url


if __name__ == '__main__':
    pool = Pool(2)
    urls = ['https://github.com/', 'https://www.python.org/', 'http://www.cnblogs.com/']
    results = pool.map(run_task, urls)
    print results

'''
Visit --> https://github.com/
Visit --> https://www.python.org/
48686 bytes received from https://www.python.org/.
Visit --> http://www.cnblogs.com/
47559 bytes received from http://www.cnblogs.com/.
82559 bytes received from https://github.com/.
['url:https://github.com/ --->finish', 'url:https://www.python.org/ --->finish', 'url:http://www.cnblogs.com/ --->finish']
'''
