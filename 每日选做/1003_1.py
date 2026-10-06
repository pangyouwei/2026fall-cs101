input_str = input().lower()
input_list = list(input_str)

ans = []
tmp = [input_list[0], 1]

for i in range(1, len(input_list)):
    if input_list[i] == input_list[i - 1]:
        tmp[1] += 1
    else:
        ans.append('(' + tmp[0] + ',' + str(tmp[1]) + ')')
        tmp = [input_list[i], 1]
ans.append('(' + tmp[0] + ',' + str(tmp[1]) + ')')

print(''.join(ans))
