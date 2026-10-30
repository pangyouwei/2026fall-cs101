class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)  # 选择
                    backtrack()  # 递归
                    sol.pop()  # 撤销选择（回溯）

        backtrack()
        return ans
