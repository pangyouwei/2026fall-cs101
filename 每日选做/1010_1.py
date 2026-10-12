matrix = [list(map(int, input().split())) for _ in range(5)]

for i in range(5):
    num = max(matrix[i])
    j = matrix[i].index(num)
    j_list = [lst[j] for lst in matrix]

    if num == min(j_list):
        print(i + 1, j + 1, num)
        break
else:
    print("not found")
