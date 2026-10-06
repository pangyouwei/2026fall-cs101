class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0

        for i in range(1, len(s)):
            depth = s[:i].count('(') - s[:i].count(')')

            max_depth = max(max_depth, depth)

        return max_depth
