N = int(input())

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1
for i in range(2, N + 1):
    for j in range(1, i + 1):
        dp[i] += dp[i - j]

print(dp[N])
