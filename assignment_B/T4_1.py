N, B = map(int, input().split())
v = list(map(int, input().split()))
w = list(map(int, input().split()))

dp = [[0] * (B + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, B + 1):
        if j >= w[i - 1]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i - 1]] + v[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

print(dp[N][B])
