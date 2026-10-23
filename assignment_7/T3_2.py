def josephus_formula(a, b):
    """递归（编号从0开始）"""
    r = 0
    for k in range(2, a + 1):
        # f(1) -> f(2) -> ... -> f(a)
        r = (r + b) % k
    return r + 1  # 莫忘+1


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    print(josephus_formula(n, m))
