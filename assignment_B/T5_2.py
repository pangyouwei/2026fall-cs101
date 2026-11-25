class Solution:
    def expand(self, s: str, l: int, r: int) -> tuple:
        n = len(s)
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s

        start, end = 0, 0
        for i in range(n):
            l1, r1 = self.expand(s, i, i)
            l2, r2 = self.expand(s, i, i + 1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]
