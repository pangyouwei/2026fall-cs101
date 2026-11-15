n = int(input())

res = []
for i in range(1, n + 1):
    i_str = str(i)
    bi_str = bin(i)[2:]
    if i_str == i_str[::-1] and bi_str == bi_str[::-1]:
        res.append(i)

print(len(res), max(res))
