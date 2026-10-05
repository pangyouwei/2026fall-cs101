mode = int(input())

if mode == 1:
    print(input())
if mode == 2:
    num = int(input())
    print(num ** 2)
if mode == 3:
    string_1, string_2, string_3 = input().split()
    print(string_3, string_2, string_1)
if mode == 4:
    num_1, num_2 = map(int, input().split())
    print(num_1 + num_2, num_1 * num_2)
if mode == 5:
    mode_5_list = [int(i) for i in input().split()]
    print(len(mode_5_list), sum(mode_5_list), max(mode_5_list))
if mode == 6:
    output_integer = 0
    while True:
        something = input()
        if something == 'END':
            break
        else:
            output_integer += int(something)
    print(output_integer)
if mode == 7:
    n = int(input())
    sum_list = []
    for i in range(n):
        num_1, num_2 = map(int, input().split())
        sum_list.append(num_1 + num_2)
    for result in sum_list:
        print(result, end=' ')
if mode == 8:
    str_1, str_2, str_3 = input().split(",")
    print(str_3, str_2, str_1)
