# two pointers
n = int(input())
height = list(map(int, input().split()))

l = 0
r = n - 1
l_max = r_max = 0
ans = 0
while l < r:
    l_max = max(l_max, height[l])
    r_max = max(r_max, height[r])
    if height[l] < height[r]:
        ans += min(l_max, r_max) - height[l]
        l += 1
    else:
        ans += min(l_max, r_max) - height[r]
        r -= 1

print(ans)
