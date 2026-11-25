while True:
    n = int(input())
    if n == 0:
        break

    t = list(map(int, input().split()))
    t.sort()
    k = list(map(int, input().split()))
    k.sort()

    ans = 0
    l1, r1 = 0, n - 1
    l2, r2 = 0, n - 1
    for _ in range(n):
        if t[r1] > k[r2]:
            ans += 1
            r1 -= 1
            r2 -= 1
        elif t[r1] < k[r2]:
            ans -= 1
            l1 += 1
            r2 -= 1
        else:
            if t[l1] > k[l2]:
                ans += 1
                l1 += 1
                l2 += 1
            else:
                if t[l1] < k[r2]:
                    ans -= 1
                l1 += 1
                r2 -= 1

    print(200 * ans)
