n = int(input())
r = list(map(int, input().split()))

res = [1] * n

for i in range(1, n):
    if r[i] > r[i - 1]:
        res[i] = res[i - 1] + 1
for j in range(n - 1, 0, -1):  # 倒序遍历
    if r[j - 1] > r[j]:
        res[j - 1] = max(res[j - 1], res[j] + 1)

print(sum(res))
