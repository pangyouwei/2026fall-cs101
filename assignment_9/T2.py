n, m = map(int, input().split())
s = ['0'] + list(input()) + ['0']
ini = s.count('1')

for _ in range(m):
    for i in range(1, n + 1):
        if s[i - 1] == '0' and s[i] == '0' and s[i + 1] == '0':
            s[i] = '1'
            break

print(s.count('1') - ini)
print(''.join(s[1:n + 1]))
