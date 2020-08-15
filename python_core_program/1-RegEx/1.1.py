# coding: utf-8

###########################################
# Copyright© All Rights Reserved.
# @Brief: 
# @Auther: 
# @Email: 
# @Date: 20200724
###########################################

import re

string = 'foo21\n-121foo23Fck7\t21fck8'

# compile



# purge



# match从字符串起始部分开始匹配
m = re.match('foo', string)
if m is not None:
    print (m)  # <_sre.SRE_Match object; span=(0, 3), match='foo'>
    print (type(m.group()))  # <class 'str'>
    print (m.group())  # foo

m2 = re.match('(\w+)(\d+)(\s)', string)
if m2 is not None:
    print (m2)  # <_sre.SRE_Match object; span=(0, 6), match='foo21\n'>
    print (m2.group(1))  # foo2
    print (m2.group(2))  # 1
    print (m2.group(3))  # \n
    print (m2.groups())  # ('foo2', '1', '\n')


# search从字符串起始部分开始搜索匹配的
s = re.search('21', string)
if s is not None:
    print (s)  # <_sre.SRE_Match object; span=(3, 5), match='21'>
    print (type(s.group()))  # <class 'str'>

# findall
fa = re.findall('foo', string)
if fa is not None:
    print (fa)  # ['foo', 'foo']
    print (type(fa))  # <class 'list'>

# finditer
fi = re.finditer('foo', string)
if fi is not None:
    print (fi)  # <callable_iterator object at 0x7fbb61322908>
    for i in fi:
        print (i)  
        # <_sre.SRE_Match object; span=(0, 3), match='foo'>
        # <_sre.SRE_Match object; span=(10, 13), match='foo'>

# sub
sb = re.sub(r'(\d\s)', 'DD2DSB', string)
if sb is not None:
    print (sb)  # foo2DD2DSB-121foo23FckDD2DSB21fck8

# subn
sbn = re.subn(r'(\d\s)', 'DD2DSB', string)
if sbn is not None:
    print (sbn)  # ('foo2DD2DSB-121foo23FckDD2DSB21fck8', 2)

# split
re_split = re.split(r'(\d\s)', string)
if re_split is not None:
    print (re_split)  # ['foo2', '1\n', '-121foo23Fck', '7\t', '21fck8']

# 扩展符号
re_sp = re.findall(r'(?im)(^th[\w]+)', 
                    "This line is the first, \
                    another line, \
                    that line, it's the best")
if re_sp is not None:
    print (re_sp)  # ['This']

