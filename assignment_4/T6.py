import math


def sieve(num: int) -> list[bool]:
    """返回布尔列表，prime_flags[i] 表示 i 是否为质数"""
    # 埃拉托斯特尼筛法
    if num < 2:
        return [False] * (num + 1)

    prime_flags = [True] * (num + 1)
    prime_flags[0] = prime_flags[1] = False

    for i in range(2, math.isqrt(num) + 1):
        if prime_flags[i]:
            for j in range(i * i, num + 1, i):
                prime_flags[j] = False

    return prime_flags


LIMIT = 10 ** 6
is_prime = sieve(LIMIT)


def is_t_prime(num):
    square = math.isqrt(num)
    if square * square == num:
        if is_prime[square]:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


n = int(input())
input_list = list(map(int, input().split()))

if __name__ == "__main__":
    for index in range(n):
        print(is_t_prime(input_list[index]))
