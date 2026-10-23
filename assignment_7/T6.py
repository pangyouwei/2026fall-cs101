t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    if m == 1:
        print(0)
        for _ in range(n):
            print(0)
    else:
        print(min(n + 1, m))

        out = []
        for i in range(min(n, m - 1)):
            # 完成“循坏移位”
            out.append([(i + j) % m for j in range(m)])
        if n > m - 1:
            for _ in range(m - 1, n):
                out.append(list(range(m)))

        for r in out:
            print(*r)
