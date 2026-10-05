class Solution:
    def countMonobit(self, n: int) -> int:
        ans = 0
        for i in range(0, n + 1):
            if bin(i)[2:].count('1') == 0 or bin(i)[2:].count('0') == 0:
                ans += 1

        return ans
