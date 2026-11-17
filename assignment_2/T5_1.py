l, n = map(int, input().split())
trees = [True] * (l + 1)  # 极耗空间，请慎重

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b + 1):
        trees[j] = False

answer = sum(trees)
print(answer)
