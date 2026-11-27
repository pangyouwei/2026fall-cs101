k = int(input())
missiles = list(map(int, input().split()))

chosen = [1] * k
unchosen = [0] * k
for i in range(k - 2, -1, -1):
    for j in range(i + 1, k):
        if missiles[j] <= missiles[i]:
            chosen[i] = max(chosen[i], chosen[j] + 1)
    unchosen[i] = max(chosen[i + 1], unchosen[i + 1])

print(max(chosen[0], unchosen[0]))
