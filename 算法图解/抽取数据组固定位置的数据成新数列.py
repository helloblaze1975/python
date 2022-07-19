# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/13  19:22
#选取固定的数据
# data=[1, 2, 3, 4, 5, 6, 7, 9]

# print(data[0],data[1],data [-2])# 第一个第二个和倒数第二个


#遇到一个数之后， 把前面的都删除
# data=[1, 2, 3, 4, 5, 6, 7, 9]
# end_game=False
# new_data=[]
# print(type(new_data))#打印出来变量的类型是str
# while not end_game:
#     for i in data:
#         if i == 3:
#             end_game = True
#         elif:
#             new_data.append(i)
#
# print new_data# 这个输出是跨过3 ，其他数都有


# data=[1, 2, 3, 4, 5, 6, 7, 9]
# new_data=[]
# boarder=data.index(3)#获取变量再数组中的索引（位置）
# print(boarder)
# for i in data(3,9):
#      new_data.append(i)
# print(new_data)




data =[1, 2, 3, 4, 5, 6, 7, 9]
new_data=data[data.index(5)+1:]
print(new_data)







