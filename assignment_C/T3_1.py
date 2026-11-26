# dp
class Solution:
    def numSquares(self, n: int) -> int:
        # 所有正整数都能拆成若干（<=4）完全平方数之和
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            cur = 4
            for j in range(1, int(i ** 0.5) + 1):
                cur = min(cur, dp[i - j * j] + 1)
        return dp[-1]
