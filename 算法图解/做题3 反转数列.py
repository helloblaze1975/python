# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/13  18:38
#

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "Geeksforgeeks"

print ("The original string  is : ")
print (s)

print ("The reversed string(using loops) is : ")
print (reverse(s))