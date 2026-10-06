p, e, i, d = map(int, input().split())

t = d + 1
while (t - p) % 23 != 0:
    t += 1
while (t - e) % 28 != 0:
    t += 23
while (t - i) % 33 != 0:
    t += 23 * 28

print(t - d)
