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
    A_i = A[i]
    C_i = C[i]
    # 提到内层循环外，减少索引
    for j in range(n):
        if A_i[j] != 0:  # 跳过0，常数优化
            B_j, v = B[j], A_i[j]
            for t in range(n):
                C_i[t] += v * B_j[t]

for r in range(n):
    for c in range(n):
        if C[r][c] != 0:
            print(r, c, C[r][c])
