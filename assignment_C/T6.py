N = int(input())
nums = []
while len(nums) < N ** 2:
    nums.extend(list(map(int, input().split())))
matrix = []
for i in range(0, N ** 2, N):
    matrix.append(nums[i:i + N])

ans = float('-inf')
for i in range(N):
    temp = [0] * N
    for j in range(i, N):
        for k in range(N):
            temp[k] += matrix[j][k]
        # kadane
        cur = temp[0]
        best = temp[0]
        for k in range(1, N):
            cur = max(temp[k], cur + temp[k])
            best = max(best, cur)
        ans = max(ans, best)

print(ans)
