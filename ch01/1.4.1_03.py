# coding:utf-8

# 3.multiprocessing模块提供了一个Pool类来代表进程池对象

import os
import random
import time
from multiprocessing import Pool


def run_task(name):
    print 'Task %s (pid = %s) is running...' % (name, os.getpid())
    time.sleep(random.random() * 3)
    print 'Task %s end.' % name


if __name__ == '__main__':
    print 'Current process %s.' % os.getpid()
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(run_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

'''
Current process 22897.
Waiting for all subprocesses done...Task 0 (pid = 22898) is running...

Task 1 (pid = 22899) is running...
Task 2 (pid = 22900) is running...
Task 0 end.
Task 3 (pid = 22898) is running...
Task 1 end.
Task 4 (pid = 22899) is running...
Task 2 end.
Task 4 end.
Task 3 end.
All subprocesses done.
'''
