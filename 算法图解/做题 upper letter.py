# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/15  21:11

#如何判断是否都是大学字母
# def is_all_upper(text):
#     # your code here
#     return text=text.upper()
#
#
#
#
# text=raw_input("input a letter")
#
# is_all_upper()


# data=[1, 2, 3, 4, 5, 6, 7, 9]
#
# data.append(data[0])
# del data[0]
#
# print(data)
a=[1, 2, 3, 4, 5, 6, 7, 9]


new_list = []
new_list2 = []


if len(a) % 2 != 0:
    a += "_"

for i in range(0, len(a), 2):
    new_list.append(a[i])
print(new_list)
for j in range (1,len(a),2):
    new_list2.append(a[j])
print(new_list2)

print()
        # new_lst.append(a[i : i + 2])



#






