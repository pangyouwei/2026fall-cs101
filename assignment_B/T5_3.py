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
        r = -1  # 已知回文可达的最右端
        j = -1  # 达到 r 的那个回文中心
        for i in range(len(s)):
            if r < i:
                cur_arm_len = self.expand(s, i, i)
            else:
                i_sym = 2 * j - i  # 找对称(symmetry)
                min_arm_len = min(arm_len[i_sym], r - i)
                cur_arm_len = self.expand(s, i - min_arm_len, i + min_arm_len)
            arm_len.append(cur_arm_len)
            if i + cur_arm_len > r:
                r = i + cur_arm_len
                j = i
            if 2 * cur_arm_len + 1 > end - start:
                start = i - cur_arm_len
                end = i + cur_arm_len

        return s[start + 1:end + 1:2]
