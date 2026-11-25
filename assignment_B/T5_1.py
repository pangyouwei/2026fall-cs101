class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        max_length = 1
        start = 0
        dp = [[False] * n for _ in range(n)]
        # 解决长度为1的
        for i in range(n):
            dp[i][i] = True
        # 解决长度为2的
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                max_length = 2
                start = i
        # 解决长度>=3的
        for length in range(3, n + 1):
            # 长子串的判断依赖短子串，故可按length正序遍历
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
                if dp[i][j]:
                    max_length = max(max_length, length)
                    start = i

        return s[start:start + max_length]
