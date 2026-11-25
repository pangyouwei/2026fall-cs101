N, B = map(int, input().split())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = [0] * (B + 1)
for i in range(N):
    for j in range(B, w[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(dp[-1])
