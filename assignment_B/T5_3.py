class Solution:
    def expand(self, s: str, l: int, r: int) -> int:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # j - i + 1 = 2 * arm_len + 1
        return (r - l - 2) // 2

    def longestPalindrome(self, s: str) -> str:
        s = '#' + '#'.join(list(s)) + '#'  # 统一奇偶情况
        end, start = -1, 0
        arm_len = []
        r = -1
        j = -1
