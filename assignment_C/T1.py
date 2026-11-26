class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]

        dp = [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1] + [0] * (i - 1) + [1]
            for j in range(1, i):
                row[j] = dp[i - 1][j - 1] + dp[i - 1][j]
            dp.append(row)

        return dp
