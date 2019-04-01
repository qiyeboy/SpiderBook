# coding:utf-8

# 1.第一种方式：使用os模块中的fork方式实现多进程

import os

if __name__ == '__main__':
    print 'current Process (%s) start ...' % (os.getpid())
    pid = os.fork()
    if pid < 0:
        print 'error in fork'
    elif pid == 0:
        print 'I am child process(%s) and my parent process is (%s)', (os.getpid(), os.getppid())
    else:
        print 'I(%s) created a child process (%s).', (os.getpid(), pid)

'''
current Process (18708) start ...
I(%s) created a child process (%s). (18708, 18709)
I am child process(%s) and my parent process is (%s) (18709, 18708)
'''
