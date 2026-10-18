# functools.cmp_to_key!
from functools import cmp_to_key


# 手搓两两比较（单挑）函数
def cmp(a, b):
    if int(a + b) > int(b + a):
        return 1
    elif int(a + b) < int(b + a):
        return -1
    else:
        return 0


n = int(input())
nums = sorted(list(input().split()), key=cmp_to_key(cmp))
# Python 3 里通过这样写实现Python 2 里cmp参数的功能
print("".join(nums[::-1]), "".join(nums))
