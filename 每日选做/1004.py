n = int(input())

ans = 0

for _ in range(n):
    ans += (input().replace('### ###', '')).count('###') // 2

print(ans)
