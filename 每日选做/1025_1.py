# dp
n = int(input())
height = list(map(int, input().split()))

leftMAX = [0] * n
leftMAX[0] = height[0]
rightMAX = [0] * n
rightMAX[n - 1] = height[n - 1]
for i in range(1, n):
    leftMAX[i] = max(leftMAX[i - 1], height[i])
for i in range(n - 2, -1, -1):
    rightMAX[i] = max(rightMAX[i + 1], height[i])

ans = sum(min(leftMAX[i], rightMAX[i]) - height[i] for i in range(n))
print(ans)
