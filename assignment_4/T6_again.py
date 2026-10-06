import math


def linear_sieve(num: int) -> list[bool]:
    """返回布尔列表，prime_flags[i] 表示 i 是否为质数"""
    # 线性筛法/欧拉筛法
    if num < 2:
        return [False] * (num + 1)

    prime_flags = [True] * (num + 1)
    prime_flags[0] = prime_flags[1] = False

    primes = []

    for i in range(2, num + 1):
        if prime_flags[i]:
            primes.append(i)

        for p in primes:
            if i * p > num:
                break
            prime_flags[i * p] = False

            if i % p == 0:
                break

    return prime_flags


LIMIT = 10 ** 6
is_prime = linear_sieve(LIMIT)


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
