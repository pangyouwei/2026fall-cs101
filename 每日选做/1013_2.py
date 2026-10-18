# 取整列数的最大位数，把所有数都扩充到最大位数后比较
from math import ceil

n = input()
nums_1 = input().split()

max_len = len(max(nums_1, key=lambda x: len(x)))
nums_1.sort(key=lambda x: tuple([int(i) for i in x]) * (ceil(2 * max_len / len(x))))
nums_2 = nums_1[::-1]

print(''.join(nums_2), ''.join(nums_1))
