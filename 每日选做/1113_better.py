class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        if not heights:
            return 0
        n = len(heights)

        left = [0] * n
        right = [n] * n
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                right[stack.pop()] = i
            left[i] = stack[-1] if stack else -1
            stack.append(i)

        ans = max(heights[i] * (right[i] - left[i] - 1) for i in range(n))
        return ans
