# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/22  13:17
def nearest_value(values, one) :
    values1 = list(values)
    diff=[abs(one-v) for v in values1]
    return values1[diff.index(min(diff))]

print(nearest_value({4,5,6}, 7))





