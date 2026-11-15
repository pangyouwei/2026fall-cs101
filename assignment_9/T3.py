import sys

sys.setrecursionlimit(1 << 20)

n, m = map(int, input().split())
grid = []
for _ in range(n):
    row = list(input())
    grid.append(row)

# 0：未访问；1：正在访问；2：确定能逃出；3：确定不能逃出
state = [[0] * m for _ in range(n)]

direction = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1)
}


def dfs(x: int, y: int) -> bool:
    if state[x][y] == 1:
        return False

    if state[x][y] == 2:
        return True
    if state[x][y] == 3:
        return False

    state[x][y] = 1
    dx, dy = direction[grid[x][y]]
    nx, ny = x + dx, y + dy
    if not (0 <= nx < n and 0 <= ny < m):
        state[x][y] = 2
        return True

    nxt_ok = dfs(nx, ny)
    if nxt_ok:
        state[x][y] = 2
        return True
    else:
        state[x][y] = 3
        return False


escape_count = 0
for i in range(n):
    for j in range(m):
        if state[i][j] == 0:
            if dfs(i, j):
                escape_count += 1
        elif state[i][j] == 2:
            escape_count += 1

print(escape_count)
