# coding=utf8
# Happy
# Huan Zhang 张焕
# Day day up!
# 22/05/19  14:40

def selectionSort(arr):
    newArr=[]
    for i in range(len(arr)):
        smallest=list.index(min(arr))
        newArr.append(arr.pop(smallest))
    return newArr


lst=[5,3, 7, 2, 10]
print(selectionSort(lst))
