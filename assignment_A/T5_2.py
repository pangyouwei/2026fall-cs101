n, a, b, c = map(int, input().split())

INF = float('-inf')
dp = [INF] * (n + 1)
dp[0] = 0
for i in range(1, n + 1):
    if i >= a:
        dp[i] = max(dp[i], dp[i - a] + 1)
    if i >= b:
        dp[i] = max(dp[i], dp[i - b] + 1)
    if i >= c:
        dp[i] = max(dp[i], dp[i - c] + 1)

print(dp[n])
