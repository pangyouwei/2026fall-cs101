n = int(input())

rules = {
    'A': 2,
    'B': 2,
    'C': 2,
    'D': 3,
    'E': 3,
    'F': 3,
    'G': 4,
    'H': 4,
    'I': 4,
    'J': 5,
    'K': 5,
    'L': 5,
    'M': 6,
    'N': 6,
    'O': 6,
    'P': 7,
    'R': 7,
    'S': 7,
    'T': 8,
    'U': 8,
    'V': 8,
    'W': 9,
    'X': 9,
    'Y': 9,
}

ans_dict = {}
for _ in range(n):
    l = list(input().replace('-', ''))
    new_l = []
    for i in range(len(l)):
        if l[i].isdigit():
            new_l.append(l[i])
        else:
            new_l.append(str(rules[l[i]]))
    s = ''.join(new_l[:3]) + '-' + ''.join(new_l[3:])
    if s in ans_dict:
        ans_dict[s] += 1
    else:
        ans_dict[s] = 1

ans_dict = dict(sorted(ans_dict.items()))

max_count = max(ans_dict.values(), default=0)
if max_count <= 1:
    print("No duplicates.")
else:
    for telephone_num in ans_dict:
        if ans_dict[telephone_num] >= 2:
            print(telephone_num, ans_dict[telephone_num])
