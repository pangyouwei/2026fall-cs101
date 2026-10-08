n = int(input())
max_l = - 10 ** 9
min_r = 10 ** 9

for _ in range(n):
    l, r = map(int, input().split())
    max_l = max(max_l, l)
    min_r = min(min_r, r)

if max_l <= min_r:
    print(max_l)
else:
    print(-1)
