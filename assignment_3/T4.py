class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n = format(n, '032b')
        bin_output_str = str(bin_n)[::-1]
        output = int(bin_output_str, 2)

        return output
