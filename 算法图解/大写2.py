# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/08  0:06
# 方法一：
# def format_name(f_name,l_name):
#      print(f_name.title())
#      print(l_name.title())

# format_name("anglea","yu")

# 方法二：
def format_name(f_name,l_name):
    C_f_name=f_name.title()
    C_l_name =l_name.title()
    return C_f_name +C_l_name

print(format_name("zhang","huan"))