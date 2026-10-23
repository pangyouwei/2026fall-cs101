# dp（动态规划）

n = int(input())
li = list(map(int, input().split()))

dpup = 1  # 当前处理到的位置，最后一段趋势为上升的最长摆动子序列长度
dpdo = 1  # 当前处理到的位置，最后一段趋势为下降的最长摆动子序列长度

for i in range(1, n):
    if li[i] > li[i - 1]:
        dpup = max(dpdo + 1, dpup)
        # dpup = dpdo + 1即可
    if li[i] < li[i - 1]:
        dpdo = max(dpup + 1, dpdo)
        # dpdo = dpup + 1即可

print(max(dpup, dpdo))
