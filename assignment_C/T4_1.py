k = int(input())
missiles = list(map(int, input().split()))

dp = [1] * k
# dp[i]: 以第i个导弹为结尾的最长不增子序列长度
for i in range(1, k):
    for j in range(i):
        if missiles[i] <= missiles[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
