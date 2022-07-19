# coding=utf8
# Happy
# Huan Zhang
# Day day up!
# 22/05/17  12:58
#我的办法
def beginning_zeros(number: str) -> int:
    # your code here
    result = 0
    for i in number:
        if int(i) != 0:

            break
        else:
            result += 1

    return result

#大佬一
def beginning_zeros(number):
    str_int = str(int(number)) #这个过程会去掉字符串前面的零
    return len(number) - len(str_int) + (str_int == '0')
    #这个bollen的值正确是1，错误是0 如果数字是零，那么会加 一

print(beginning_zeros("0670881"))

#大佬二
def beginning_zeros2(number):
    return len(number) - len(number.lstrip('0'))
#lstrip截掉字符串左边的空格或指定字符。

print(beginning_zeros2("0"))




