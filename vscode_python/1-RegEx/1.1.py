import re

# match从字符串起始部分开始匹配
m = re.match('.*\n$', 'foo123\n')
if m is not None:
    print (m.group())


#search
s = re.search('\n', 'foo123\n123\n')
if s is not None:
    print (s.group())
    # print (s.group(0))
    # print (s.group(1))
    # print (s.groups())