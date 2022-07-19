# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/13  17:25
# num = str(raw_input('a number'))
# print(num)
# a=len(num)
# print(a)
# num2=num.strip("0")
# print(num2)
# b=len(num2)
# print(b)
# print(a-b)


num = str(raw_input('a number'))
n = str(num)
print(len(n) - len(n.strip('0')))