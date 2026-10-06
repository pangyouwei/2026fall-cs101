n = int(input())
input_list = input().split()

ans = []
tmp = input_list[0] + ' '
for i in input_list[1:]:
    if len(tmp) + len(i) > 80:
        ans.append(tmp.rstrip())
        tmp = i + ' '
    else:
        tmp += i + ' '
ans.append(tmp.rstrip())

print('\n'.join(ans))
