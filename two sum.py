nums = [1, 2, 3, 4]
target = 4
#遍历的方法，空间复杂度小，时间复杂度大
# for i in nums:
#     j = target -i
#     start_index = nums.index(i)
#     next_index = start_index + 1
#     temp_nums = nums[next_index:]
#     if j in temp_nums:
#         print(nums.index(i), next_index + temp_nums.index(j))
# 用dic的方法来记录index
nums = [11, 22, 33, 23]
target = 44
dic = {}
for i in range(len(nums)):
    if target-nums[i] not in dic:
        dic[nums[i]] = i
        print("i:",i,"nums[i]:",nums[i],"target-i:",{target-nums[i]})
        print(dic)
    else:
        print(i)
        temp = target -nums[i]
        print(dic[temp])
        break


#     if remaining in seen:  # 3
#         print([i, seen[remaining]])  # 4
#     else:
#         seen[value] = i  # 5
# print(seen)