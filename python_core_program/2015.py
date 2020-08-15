# coding: utf-8

#########################################
# 小明2015年的年纪 = 出生年份的数字之和
#########################################

# 10年分类讨论
# 出生年份2010-2015，2015-201x=3+x => 5-x=3+x => x=1
# 出生年份2000-2009，2015-200x=2+x => 15-x=2+x => x=6.5
# 出生年份1990-1999，2015-199x=19+x => 25-x=19+x => x=3
# 出生年份1980-1989，2015-198x=18+x => 35-x=18+x => x=8.5
# 出生年份1970-1979，2015-197x=17+x => 45-x=17+x => x=14.0


# for i in range(201):
#     x=((5+10*i)-((201-i)//100+(201-i)%100//10+(201-i)%10))/2
#     if x > 10:
#         break
#     if x%1 == 0:
#         print ("小明出生年份：{}{}".format((201-i),int(x)))

def getBirthYear(year):
    for i in range(year):
        age = i
        birthYear = year - i
        sumBirthYear = 0
        for numb in str(birthYear):
            sumBirthYear += int(numb)
        if sumBirthYear == age:
            print ("小明出生年份：{}".format(birthYear))

getBirthYear(2015)