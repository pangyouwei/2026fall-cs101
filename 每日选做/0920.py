mode, rule = map(int, input().split())
if mode == 1:
    n = int(input())
    nums = list(map(int, input().split()))
    if rule == 1:
        nums.sort()
    if rule == 2:
        nums.sort(reverse=True)
    print(*nums)
    print(max(nums), min(nums))
if mode == 2:
    n = int(input())
    strs = input().split()
    if rule == 1:
        strs.sort()
    if rule == 2:
        strs.sort(reverse=True)
    print(*strs)
if mode == 3:
    n = int(input())
    tuples = {}
    for _ in range(n):
        a, b = map(int, input().split())
        tuples[(a, b)] = a + b
    if rule == 1:
        tuples = dict(sorted(tuples.items(), key=lambda x: x[1]))
    if rule == 2:
        tuples = dict(sorted(tuples.items(), key=lambda x: x[1], reverse=True))
    for key in tuples:
        print(*key)
if mode == 4:
    n = int(input())
    lists = []
    for _ in range(n):
        lists.append(list(map(int, input().split())))
    if rule == 1:
        lists.sort(key=lambda x: x[1])
    if rule == 2:
        lists.sort(key=lambda x: x[1], reverse=True)
    for lst in lists:
        print(*lst)
if mode == 5:
    n = int(input())
    list_1 = list(map(int, input().split()))
    list_2 = []
    if rule == 1:
        list_2 = sorted(list_1)
    if rule == 2:
        list_2 = sorted(list_1, reverse=True)
    print(*list_1)
    print(*list_2)
if mode == 6:
    n = int(input())
    tuples = []
    for _ in range(n):
        a, b = map(int, input().split())
        tuples.append((a, b))
    if rule == 1:
        tuples.sort(key=lambda x: x[1], reverse=True)
        tuples.sort(key=lambda x: x[0])
    if rule == 2:
        tuples.sort(key=lambda x: x[1])
        tuples.sort(key=lambda x: x[0], reverse=True)
    for tpl in tuples:
        print(*tpl)
