class Solution:
    def countMonobit(self, n: int) -> int:
        i = 0
        cnt = 0
        while 2 ** i - 1 <= n:
            i += 1
            cnt += 1
        return cnt
