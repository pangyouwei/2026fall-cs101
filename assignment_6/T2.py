p = int(input())
weapons = list(map(int, input().split()))
weapons.sort()

l = 0
r = len(weapons) - 1
cur = 0
ans = 0
while l <= r:
    if p - weapons[l] < 0:
        if cur >= 1:
            p += weapons[r]
            r -= 1
            cur -= 1
        else:
            break
    else:
        p -= weapons[l]
        l += 1
        cur += 1
        ans = cur

print(ans)
