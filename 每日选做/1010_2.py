# 转置矩阵法！！！
matrix_1 = [list(map(int, input().split())) for _ in range(5)]
matrix_2 = [list(col) for col in zip(*matrix_1)]

for i in range(5):
    num = max(matrix_1[i])
    j = matrix_1[i].index(num)

    if num == min(matrix_2[j]):
        print(i + 1, j + 1, num)
        break
else:
    print("not found")
