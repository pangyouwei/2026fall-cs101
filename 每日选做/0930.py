input_list = list(input())

i = 0
num_list = []

while i < len(input_list):
    if input_list[i].isdigit():
        num_list.append(input_list[i])
    else:
        if num_list:
            print(int(''.join(num_list)))
        num_list = []

    i += 1
if num_list:
    print(int(''.join(num_list)))
