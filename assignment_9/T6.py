s = input()
n = len(s)

# prefix sum
sums = [0]
for i in range(n):
    sums.append(sums[i] + (1 if s[i] == '(' else -1))
# monotonic stack
nxt = [n] * n
stack = []
for i, x in enumerate(sums):
    while stack and sums[stack[-1]] > x:
        j = stack.pop()
        nxt[j] = i
    stack.append(i)

q = int(input())
out = []
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    out.append("YES" if sums[r + 1] == sums[l] and r < nxt[l] else "NO")

print("\n".join(out))
