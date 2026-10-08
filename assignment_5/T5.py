n, C = map(int, input().split())
students = list(map(int, input().split()))
students.sort(reverse=True)

l = 0
r = n - 1
ans = 0

while l <= r:
    if students[l] + students[r] <= C:
        l += 1
        r -= 1
    else:
        l += 1
    ans += 1

print(ans)
