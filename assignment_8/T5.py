cols = [0] * 8
placement = []


def dfs(row):
    if row == 8:
        placement.append(int("".join(str(c + 1) for c in cols)))
        return

    for col in range(8):
        for i in range(row):
            if cols[i] == col or abs(cols[i] - col) == row - i:
                break
        else:
            cols[row] = col
            dfs(row + 1)
            cols[row] = 0


dfs(0)
n = int(input())
for _ in range(n):
    k = int(input())
    print(placement[k - 1])
