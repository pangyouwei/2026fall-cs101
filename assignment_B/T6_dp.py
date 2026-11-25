# 尝试用 dp 解题，可降低思考难度
while True:
    n = int(input())
    if n == 0:
        break

    t = list(map(int, input().split()))
    t.sort(reverse=True)
    k = list(map(int, input().split()))
    k.sort(reverse=True)

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    # dp[i][j]表示田忌的前i匹马vs齐王的前j匹马（部分出战部分不出战）所得最佳“权重”
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if t[i - 1] > k[j - 1]:
                w = 2
            elif t[i - 1] == k[j - 1]:
                w = 1
            else:
                w = 0
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1] + w)

    print(200 * (dp[n][n] - n))
    # dp[n][n]必须是所有马全出战所得的结果
