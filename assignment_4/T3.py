t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(y) for y in input().split()]

    minimum_1 = sum(a) + n * min(b)
    minimum_2 = sum(b) + n * min(a)

    ans = min(minimum_1, minimum_2)
    print(ans)
