import bisect

k = int(input())
missiles = list(map(int, input().split()))

tails = []
for m in reversed(missiles):
    pos = bisect.bisect_right(tails, m)
    if pos == len(tails):
        tails.append(m)
    else:
        tails[pos] = m

print(len(tails))
