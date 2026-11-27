T = int(input())

for _ in range(T):
    E, F = map(int, input().split())
    TOTAL = F - E
    N = int(input())

    INF = float('inf')
    dp = [INF] * (TOTAL + 1)
    dp[0] = 0
    for j in range(N):
        P, W = map(int, input().split())
        for i in range(W, TOTAL + 1):
            if dp[i - W] != INF:
                dp[i] = min(dp[i], dp[i - W] + P)

    if dp[-1] != INF:
        print(f"The minimum amount of money in the piggy-bank is {dp[-1]}.")
    else:
        print(f"This is impossible.")
