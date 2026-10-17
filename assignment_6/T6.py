n = int(input())
trees = [tuple(map(int, input().split())) for _ in range(n)]

if n <= 2:
    print(n)
else:
    ans = 2
    last_r = trees[0][0]

    for i in range(1, n - 1):
        # 从左到右依次处理，左边情况已知->考虑右边
        x_i, h_i = trees[i]
        l_length = x_i - last_r
        r_length = trees[i + 1][0] - x_i

        if h_i < l_length:
            ans += 1
            last_r = x_i
        elif h_i < r_length:
            ans += 1
            last_r = x_i + h_i
        else:
            last_r = x_i

    print(ans)
