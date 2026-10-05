while True:
    packages = list(map(int, input().split()))
    if packages == [0, 0, 0, 0, 0, 0]:
        break

    c1, c2, c3, c4, c5, c6 = packages
    ans = c6 + c5 + c4 + (c3 + 4 - 1) // 4

    u = [0, 5, 3, 1]
    available_2 = c4 * 5 + u[c3 % 4]
    if c2 > available_2:
        ans += ((c2 - available_2) + 9 - 1) // 9
    used_area = 36 * c6 + 25 * c5 + 16 * c4 + 9 * c3 + 4 * c2
    available_1 = 36 * ans - used_area
    if c1 > available_1:
        ans += ((c1 - available_1) + 36 - 1) // 36

    print(ans)
