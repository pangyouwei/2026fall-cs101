def josephus_formula(a, b):
    """递推（编号从1开始）"""
    if a == 1:
        return 1
    return (josephus_formula(a - 1, b) - 1 + b) % a + 1


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    print(josephus_formula(n, m))
