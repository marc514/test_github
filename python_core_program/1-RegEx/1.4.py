# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200730
###########################################

import re
import os

# os.system('who > whodata.txt')
# f = open('whodata.txt', 'r')

# f = os.popen('who', 'r')  # popen代替open
# for eachLine in f:
#     print (re.split(r'\s\s+', eachLine.strip()))
# f.close

with os.popen('who', 'r') as f: # with 代替close
    for eachLine in f:
        print (re.split(r'\s\s+', eachLine.strip()))

