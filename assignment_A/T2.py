L, M = map(int, input().split())

ranges = []
for _ in range(M):
    l, r = map(int, input().split())
    ranges.append((l, r))
ranges.sort(key=lambda x: x[0])
occupied = 0
pre_l, pre_r = ranges[0]
for l, r in ranges[1:]:
    if l <= pre_r:
        pre_r = max(pre_r, r)
    else:
        occupied += pre_r - pre_l + 1
        pre_l, pre_r = l, r
occupied += pre_r - pre_l + 1

ans = L + 1 - occupied
print(ans)
