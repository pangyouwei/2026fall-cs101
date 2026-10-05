class NumArray:

    def __init__(self, nums: list[int]):
        # 前缀和
        self.sums = [0]

        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.sums[right + 1] - self.sums[left]
