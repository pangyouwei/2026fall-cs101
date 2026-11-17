n, a, b, c = map(int, input().split())
a, b, c = sorted([a, b, c], reverse=True)
ans = 0

if a == 1 or b == 1 or c == 1:
    print(n)
    exit(0)
for i in range(n // a + 1):
    for j in range((n - i * a) // b + 1):
        rest = n - i * a - j * b
        if rest >= 0 and rest % c == 0:
            k = rest // c
            ans = max(ans, i + j + k)

print(ans)
