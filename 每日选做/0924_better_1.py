class Solution:
    # 找的都是形如2 ** k - 1的数(k = 0, 1, 2, ...)
    def countMonobit(self, n: int) -> int:
        return (n + 1).bit_length()
        # floor(log2(n)) = n.bit_length() - 1
