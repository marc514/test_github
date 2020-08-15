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

loops = [1,2,3,4,5]
total = 0

def loop(nloop, nsec, lock):
    global total
    # print('start loop {} at: {}'.format(nloop, ctime()))
    # sleep(nsec)
    total += nsec
    # print('loop {} done at: {}'.format(nloop, ctime()))
    print('loop {} done at: {}'.format(nloop+1, total))
    lock.release()

def main():
    print('main start at: ', ctime())
    locks = []

    for i in range(len(loops)):
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    for i in range(len(loops)):
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    for i in range(len(loops)):
        while locks[i].locked():
            pass

    # print('all done at: ', ctime())
    print('all done at: ', total)

if __name__ == "__main__":
    main()
