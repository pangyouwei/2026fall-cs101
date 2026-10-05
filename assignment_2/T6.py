import math

while True:
    n = int(input())
    if n == 0:
        break

    ans = float("inf")
    for _ in range(n):
        v, t = map(int, input().split())
        if t >= 0:
            arrival_time = (4500 * 3.6) / v + t
            ans = min(ans, arrival_time)

    print(math.ceil(ans))
