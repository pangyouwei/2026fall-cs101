class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]
        ps_set = set(ps)

        def divisible(n: int, count: int) -> bool:
            if count == 1:
                return n in ps_set
            for p in ps:
                if divisible(n - p, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if divisible(n, count):
                return count
        return -1
