d = int(input())
n = int(input())
trashes = {}
x_max = 0
x_min = 0
y_max = 0
y_min = 0
for _ in range(n):
    x, y, i = map(int, input().split())
    x_max = max(x_max, x)
    x_min = min(x_min, x)
    y_max = max(y_max, y)
    y_min = min(y_min, y)
    trashes[(x, y)] = i
c = x_max - x_min + 1 + 2 * d
r = y_max - y_min + 1 + 2 * d
matrix = [[0] * c for _ in range(r)]

DIRS = tuple((di, dj) for di in range(- d, d + 1) for dj in range(- d, d + 1))
for (x, y) in trashes.keys():
    for d_i, d_j in DIRS:
        matrix[y - y_min + d + d_i][x - x_min + d + d_j] += trashes[(x, y)]
ans_2 = 0
for i in range(r):
    for j in range(c):
        if 0 <= y_min - d + i <= 1024 and 0 <= x_min - d + j <= 1024:
            ans_2 = max(ans_2, matrix[i][j])
ans_1 = 0
for i in range(r):
    for j in range(c):
        if 0 <= y_min - d + i <= 1024 and 0 <= x_min - d + j <= 1024:
            if matrix[i][j] == ans_2:
                ans_1 += 1

print(ans_1, ans_2)
