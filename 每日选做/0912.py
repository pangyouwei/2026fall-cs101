n = int(input())
input_list = [int(i) for i in input().split()]


def volume_fraction(num, given_list):
    return sum(given_list) / num


print(volume_fraction(n, input_list))
