# dp
class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        for i in range(n):
            if ((i + 1) ** 0.5) % 1 == 0:
                squares.append(i + 1)

        # 所有正整数都能拆成若干（<=4）完全平方数之和
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            cur = 4
            idx = 0
            while 0 <= idx < len(squares) and squares[idx] <= i:
                cur = min(cur, dp[i - squares[idx]] + 1)
                idx += 1
            dp[i] = cur

        return dp[-1]
