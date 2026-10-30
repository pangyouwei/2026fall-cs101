MOD = 32767
n = int(input())
queries = [int(input()) for _ in range(n)]
max_k = max(queries)

# 递归易爆栈，换用迭代
pell = [0] * (max_k + 1)
if max_k >= 1:
    pell[1] = 1
if max_k >= 2:
    pell[2] = 2
for i in range(3, max_k + 1):
    pell[i] = (2 * pell[i - 1] + pell[i - 2]) % MOD

ans = [pell[k] for k in queries]
for num in ans:
    print(num)
