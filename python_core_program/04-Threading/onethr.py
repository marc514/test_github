# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200811
###########################################

# import thread  # python2
# import _thread  # python3
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
    loop0()
    loop1()
    print('all done at: ', ctime())

if __name__ == "__main__":
    main()