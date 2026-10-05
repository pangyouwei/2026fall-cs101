n, k = map(int, input().split())
scores = list(map(int, input().split()))
ans = 0
for score in scores:
    if score > 0 and score >= scores[k - 1]:
        ans += 1
print(ans)
