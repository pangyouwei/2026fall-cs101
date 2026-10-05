rules = {
    0: 'Sunday',
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
}

n = int(input())
for _ in range(n):
    s = input()
    year = int(s[0:4])
    m = int(s[4:6])
    d = int(s[6:8])
    if m == 1 or m == 2:
        m += 12
        year -= 1
    c = int(str(year)[0:2])
    y = int(str(year)[2:4])

    w = (y + y // 4 + c // 4 - 2 * c + (26 * (m + 1)) // 10 + d - 1) % 7
    print(rules[w])
