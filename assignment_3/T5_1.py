class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        arr.sort()
        arr.sort(key=lambda x: bin(x).count('1'))

        return arr
