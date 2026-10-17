n, m1, m2 = map(int, input().split())
A = [[0] * n for _ in range(n)]
B = [[0] * n for _ in range(n)]
for _ in range(m1):
    r, c, num = map(int, input().split())
    A[r][c] = num
for _ in range(m2):
    r, c, num = map(int, input().split())
    B[r][c] = num

C = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

for r in range(n):
    for c in range(n):
        if C[r][c] != 0:
            print(r, c, C[r][c])
