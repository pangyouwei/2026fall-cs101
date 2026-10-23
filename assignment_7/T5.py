def sgn(x: int) -> int:
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


n = int(input())
ratings = list(map(int, input().split()))
delta = [0] + [sgn(ratings[i + 1] - ratings[i]) for i in range(n - 1)] + [0]
candies = [0 for _ in range(n)]
mins = []

for i in range(n):
    if delta[i] <= 0 <= delta[i + 1]:
        mins.append(i)
for i in range(n):
    if i in mins:
        candies[i] = 1
    if delta[i] > 0 and delta[i + 1] >= 0:
        a = max(a for a in mins if a < i)
        candies[i] = i - a + 1
    if delta[i] <= 0 and delta[i + 1] < 0:
        b = min(b for b in mins if b > i)
        candies[i] = b - i + 1
    if delta[i] > 0 > delta[i + 1]:
        a = max(a for a in mins if a < i)
        b = min(b for b in mins if b > i)
        candies[i] = max(i - a + 1, b - i + 1)

print(sum(candies))
