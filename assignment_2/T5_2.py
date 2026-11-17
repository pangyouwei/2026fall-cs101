l, n = map(int, input().split())
intervals = []
for _ in range(n):
    a, b = map(int, input().split())
    intervals.append((a, b))

intervals.sort()

total_removed = 0
if n > 0:
    cur_a, cur_b = intervals[0]
    for i in range(1, n):
        a, b = intervals[i]
        if a <= cur_b + 1:
            cur_b = max(cur_b, b)
        else:
            total_removed += (cur_b - cur_a + 1)
            cur_a, cur_b = a, b
    total_removed += (cur_b - cur_a + 1)

print(l + 1 - total_removed)
