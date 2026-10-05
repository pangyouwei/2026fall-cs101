class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((ord('{') - ord(character)) * i for i, character in enumerate(s, 1))
