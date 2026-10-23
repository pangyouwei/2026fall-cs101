def sgn(x: int) -> int:
    """便捷的正负判断函数"""
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


n = int(input())
nums = list(map(int, input().split()))
diffs = [sgn(nums[i + 1] - nums[i]) for i in range(n - 1)]

# 不太优雅...
marks = diffs.count(0)
diffs = [x for x in diffs if x != 0]
for i in range(len(diffs) - 1):
    if diffs[i] == diffs[i + 1]:
        marks += 1

print(n - marks)
