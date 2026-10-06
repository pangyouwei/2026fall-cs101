# Two pointers
s = list(input().lower()) + ['0']

a, b = 0, -1
ans = []

for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        a = i - 1
        ans.append("(%s,%d)" % (s[i - 1], a - b))
        b = a

print(''.join(ans))
