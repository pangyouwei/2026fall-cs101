class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack(i):
            # 多叉树
            ans.append(sol[:])

            for i in range(i, n):
                sol.append(nums[i])
                backtrack(i + 1)
                sol.pop()

        backtrack(0)
        return ans
