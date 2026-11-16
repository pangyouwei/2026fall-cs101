L, M = map(int, input().split())

ini_ranges = []
ranges = []
for _ in range(M):
    l, r = map(int, input().split())
    ini_ranges.append([l, r])
ini_ranges.sort(key=lambda x: x[0])
for area in ini_ranges:
    l, r = area[0], area[1]
    if not ranges or (l > ranges[-1][1] or r < ranges[-1][0]):
        ranges.append([l, r])
    else:
        ranges[-1][0] = min(ranges[-1][0], l)
        ranges[-1][1] = max(ranges[-1][1], r)

occupied = 0
for area in ranges:
    occupied += area[1] - area[0] + 1
ans = L + 1 - occupied
print(ans)
