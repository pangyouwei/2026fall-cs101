# dp
class Solution:
    def numSquares(self, n: int) -> int:
        INF = float('inf')
        dp = [INF] * (n + 1)
        dp[0] = 0

        k = 1
        while k ** 2 <= n:
            sq = k ** 2
            for a in range(sq, n + 1):
                dp[a] = min(dp[a], dp[a - sq] + 1)
            k += 1

        if dp[n] != INF:
            return dp[n]
        return -1
