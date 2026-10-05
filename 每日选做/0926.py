rules = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31,
}

n = int(input())
for _ in range(n):
    initial_month, initial_day, initial_number, final_month, final_day = map(int, input().split())
    times = 0
    if final_month > initial_month:
        for month in range(initial_month + 1, final_month):
            times += rules[month]
        times += (rules[initial_month] - initial_day) + final_day
    else:
        times = final_day - initial_day
    final_number = initial_number * (2 ** times)

    print(final_number)
