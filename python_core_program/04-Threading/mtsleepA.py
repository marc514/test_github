# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200811
###########################################

# import thread  # python2
import _thread  # python3
# import threading

from time import sleep, ctime

def loop0():
    print('start loop 0 at: ', ctime())
    sleep(4)
    print('loop 0 done at: ', ctime())

def loop1():
    print('start loop 1 at: ', ctime())
    sleep(2)
    print('loop 1 done at: ', ctime())

def main():
    print('main start at: ', ctime())
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    sleep(6)
    print('all done at: ', ctime())

if __name__ == "__main__":
    main()
