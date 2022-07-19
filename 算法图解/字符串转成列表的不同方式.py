# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/17  11:14
#把string 变成list, 并且随意搭配
# nums = raw_input("number")
s='123456'   #把字符串每一个里面的内容转成数据表的一个个元素
s_lst=list(s)
print(s_lst)
result = []

f='4567'#把字符串转成数字
print(int(f))

str_1="pan qing san"#根据空格来拆分字符串为list
print(str_1.split( ))
print(str_1.split('n'))


def get_digits(n): #把一个大的整数，变成各个数位上的数字list
    if n > 0:
        result.insert(0, n % 10)
        get_digits(n / 10)


get_digits(12345)
print(result)
