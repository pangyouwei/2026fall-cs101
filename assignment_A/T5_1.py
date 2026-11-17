n, a, b ,c = map(int, input().split())
lst = [a, b, c]

INF = float('-inf')
dp = [INF] * (n + 1)
dp[0] = 0
for w in lst:
    for j in range(w, n + 1):
        if dp[j - w] != INF:
            dp[j] = max(dp[j], dp[j - w] + 1)

print(dp[n])
