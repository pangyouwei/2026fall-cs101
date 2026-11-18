class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)

        max_areas = [0] * n
        right = [n] * n
        stack_1 = []
        for i in range(n):
            while stack_1 and heights[stack_1[-1]] > heights[i]:
                j = stack_1.pop()
                right[j] = i
            stack_1.append(i)
        left = [-1] * n
        stack_2 = []
        for i in range(n - 1, -1, -1):
            while stack_2 and heights[stack_2[-1]] > heights[i]:
                j = stack_2.pop()
                left[j] = i
            stack_2.append(i)
        for i in range(n):
            max_areas[i] = heights[i] * (right[i] - left[i] - 1)

        ans = max(max_areas)
        return ans
