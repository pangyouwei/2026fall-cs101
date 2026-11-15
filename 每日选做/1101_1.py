class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack(i):
            # 二叉树
            if i == n:
                ans.append(sol[:])
                return

            backtrack(i + 1)

            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()

        backtrack(0)
        return ans
