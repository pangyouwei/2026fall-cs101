n = int(input())
nums = input().split()

# n <= 1000, 故而O(n^2)尚可
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] + nums[j] < nums[j] + nums[i]:
            nums[i], nums[j] = nums[j], nums[i]

ans = "".join(nums)
nums.reverse()
print(ans + " " + "".join(nums))
