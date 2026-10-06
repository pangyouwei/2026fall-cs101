p, e, i, d = map(int, input().split())

t = d + 1
while True:
    if (t - p) % 23 == 0 and (t - e) % 28 == 0 and (t - i) % 33 == 0:
        print(t - d)
        break
    t += 1
