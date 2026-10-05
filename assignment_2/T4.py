for i in range(1, 6):
    row = list(map(int, input().split()))
    if 1 in row:
        j = row.index(1) + 1
        print(abs(i - 3) + abs(j - 3))
        break
