class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        ans, sol = [], []
        used = [False] * n

        def backtrack():
            if len(sol) == n:
                ans.append(sol[:])
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    sol.append(nums[i])  # 选择
                    backtrack()  # 递归
                    sol.pop()  # 撤销选择（回溯）
                    used[i] = False

        backtrack()
        return ans
