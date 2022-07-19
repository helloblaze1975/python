# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/21  6:43
def sum(list):#利用递归函数来计算和
    if list == []:
        return 0
    return list[0] + sum(list[1:])

a=[2,3,4,]
print(sum(a))

def len(list):#利用递归函数来计算元素数
    if list==[]:
        return 0
    return 1+len(list[1:])
print(len(a))


def max(list): #利用递归函数来计算最大值

    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]

    sub_max = max(list[1:])
    return list[0] if list[0] > sub_max else sub_max

print max(a)
