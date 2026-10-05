n = int(input())
print(n)

for _ in range(n):
    input_list = input().replace('.', ' ').split()
    day1, month1, year1 = int(input_list[0]), input_list[1], int(input_list[2])

    rule_1 = {
        'pop': 1,
        'no': 2,
        'zip': 3,
        'zotz': 4,
        'tzec': 5,
        'xul': 6,
        'yoxkin': 7,
        'mol': 8,
        'chen': 9,
        'yax': 10,
        'zac': 11,
        'ceh': 12,
        'mac': 13,
        'kankin': 14,
        'muan': 15,
        'pax': 16,
        'koyab': 17,
        'cumhu': 18,
        'uayet': 19,
    }
    rule_2 = {
        1: 'imix',
        2: 'ik',
        3: 'akbal',
        4: 'kan',
        5: 'chicchan',
        6: 'cimi',
        7: 'manik',
        8: 'lamat',
        9: 'muluk',
        10: 'ok',
        11: 'chuen',
        12: 'eb',
        13: 'ben',
        14: 'ix',
        15: 'mem',
        16: 'cib',
        17: 'caban',
        18: 'eznab',
        19: 'canac',
        20: 'ahau',
    }

    absolute_date = 365 * year1 + 20 * (rule_1[month1] - 1) + day1
    year2 = absolute_date // 260
    remainder = absolute_date % 260
    a2 = remainder % 13 + 1 if remainder != 0 else 1
    b2 = rule_2[remainder % 20 + 1 if remainder != 0 else 1]

    print(a2, b2, year2)
