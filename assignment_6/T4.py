n, m = map(int, input().split())
ini_matrix = [[0] + list(map(int, input().split())) + [0] for _ in range(n)]
matrix = [[0] * (m + 2)] + ini_matrix + [[0] * (m + 2)]

ans = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i][j] == 1:
            ans += 4 - (matrix[i - 1][j] + matrix[i + 1][j] + matrix[i][j - 1] + matrix[i][j + 1])

print(ans)
