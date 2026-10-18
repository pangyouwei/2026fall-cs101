# 最数学的方法...
n = int(input())
nums = input().split()

nums.sort(key=lambda x: (int(x)) / (10 ** len(x) - 1))

print(''.join(nums[::-1]), ''.join(nums))
