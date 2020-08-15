# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200724
###########################################

from random import randrange, choice  # choice随机选取
from string import ascii_lowercase as lc  # 26个小写字母字符串
from time import ctime

tlds = ('com','edu','net','org','gov')

for i in range(randrange(5, 11)):
    print ('生成序号i={}'.format(i))
    dtint = randrange((10**16))
    print (dtint)
    dtstr = ctime(dtint)
    llen = randrange(4, 8)
    login = ''.join(choice(lc) for j in range(llen)) # join合并成一个字符串
    dlen = randrange(4, 8)
    dom = ''.join(choice(lc) for j in range(dlen))
    print ('{}::{}@{}.{}::{}-{}-{}'.format(dtstr, login, dom, 
                                choice(tlds), dtint, llen, dlen))