n, m = map(int, input().split())
televisions = list(map(int, input().split()))
televisions.sort()

ans = 0

for i in range(m):
    if televisions[i] > 0:
        break
    ans += televisions[i]
print(- ans)
