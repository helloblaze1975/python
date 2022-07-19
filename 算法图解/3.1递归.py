# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/20  10:19
#Of(n!)递增的速度好快
def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x-1)


print(fact(16)/60/60/365)
#16秒能编程663457年
