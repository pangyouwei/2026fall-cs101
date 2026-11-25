class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        n = len(nums)

        dp = [0] * n
        dp[-1] = nums[-1]
        counter = [0] * n
        counter[-1] = nums[-1]
        if n == 1:
            return dp[-1]
        else:
            for i in range(n - 2, -1, -1):
                if nums[i] == 0:
                    dp[i] = 0
                    counter[i] = 0
                elif nums[i] > 0:
                    dp[i] = max(dp[i + 1] * nums[i], nums[i])
                    counter[i] = min(counter[i + 1] * nums[i], nums[i])
                else:
                    dp[i] = max(counter[i + 1] * nums[i], nums[i])
                    counter[i] = min(dp[i + 1] * nums[i], nums[i])

        return max(dp)
