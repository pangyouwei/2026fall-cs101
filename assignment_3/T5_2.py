class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        l = [(bin(i).count('1'), i) for i in arr]
        l.sort()

        return [n[1] for n in l]
