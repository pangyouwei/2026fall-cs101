from collections import deque

n = int(input())
ans = deque()

for i in range(n):
    ans.appendleft(n - i)
    ans.rotate(1)

print(*ans)
