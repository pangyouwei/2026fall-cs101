# 「四平方和定理」的加强版
class Solution:
    def checkAnswer4(self, x):
        while x % 4 == 0:
            x //= 4
        return x % 8 == 7

    def numSquares(self, n: int) -> int:
        if (n ** 0.5) % 1 == 0:
            return 1
        if self.checkAnswer4(n):
            return 4
        for i in range(1, int(n ** 0.5) + 1):
            if ((n - i * i) ** 0.5) % 1 == 0:
                return 2
        return 3
