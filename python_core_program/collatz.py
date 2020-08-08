from sys import maxsize
from time import time


def getCollatzLen(s_num, num):
    dict_len = {}
    max_len = 1
    max_num = 1
    
    for i in range(s_num+2, num):
        len_list = 1
        num_dict = i
        while (i > 1):
            if i in dict_len:
                len_list += dict_len[i]-1
                break
            else:
                if (i%2 == 0):
                    i = i/2
                else :
                    i = i*3 + 1
                len_list += 1
        dict_len[num_dict] = len_list

        if len_list > max_len:
            max_len = len_list
            max_num = num_dict

    return (max_num, max_len)

# start = time()
# (max_num, max_len) = getCollatzLen(0, 10**6)
# print (max_num, max_len)
# end = time()
# print ('程序执行时间: ',end - start)



def getCollatzList(num):
    collatzList = [num]
    while (num > 1):
        if (num%2 == 0):
            num = num/2
        else :
            num = num*3 + 1
        collatzList.append(num)
    return collatzList

print (getCollatzList(10))
