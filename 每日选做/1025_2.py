# monotonic stack
n = int(input())
height = list(map(int, input().split()))

ans = 0
stack = []
for i in range(n):
    while stack and height[stack[-1]] < height[i]:
        j = stack.pop()
        if not stack:
            break
        l = stack[-1]
        h = min(height[l], height[i]) - height[j]
        w = i - l - 1
        ans += h * w
    stack.append(i)

print(ans)
