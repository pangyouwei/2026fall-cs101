n = int(input())
hashtable = {}
for _ in range(n):
    input_list = input().split()
    stu_number = input_list[0]
    month = int(input_list[1])
    date = int(input_list[2])

    if (month, date) in hashtable:
        hashtable[(month, date)].append(stu_number)
    else:
        hashtable[(month, date)] = [stu_number]

hashtable = dict(sorted(hashtable.items(), key=lambda x: x[0]))
for (month, date), students in hashtable.items():
    if len(students) > 1:
        print(month, date, ' '.join(students))
