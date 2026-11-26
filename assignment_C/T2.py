n, m = map(int, input().split())
a = list(map(int, input().split()))

visited = {a[-1]}
dp = [0] * n
dp[-1] = 1
for i in range(n - 2, -1, -1):
    if a[i] not in visited:
        visited.add(a[i])
        dp[i] = dp[i + 1] + 1
    else:
        dp[i] = dp[i + 1]

for _ in range(m):
    l = int(input())
    print(dp[l - 1])
