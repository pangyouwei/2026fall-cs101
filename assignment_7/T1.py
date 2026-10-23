n, m = map(int, input().split())
ini_matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
matrix = [[0] * (m + 2)] + ini_matrix + [[0] * (m + 2)]
copied_matrix = [row[:] for row in matrix]

DIRS8 = tuple((di, dj) for di in (-1, 0, 1) for dj in (-1, 0, 1) if (di, dj) != (0, 0))
for i in range(1, n + 1):
    for j in range(1, m + 1):
        alive = sum(matrix[i + d_i][j + d_j] for d_i, d_j in DIRS8)
        if matrix[i][j] == 1:
            if alive < 2 or alive > 3:
                copied_matrix[i][j] = 0
        else:
            if alive == 3:
                copied_matrix[i][j] = 1

for _ in range(1, n + 1):
    print(*copied_matrix[_][1:m + 1])
