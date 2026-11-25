from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(n: int, k: int, start: int) -> int:
    if k == 0:
        return 1 if n == 0 else 0
    count = 0
    for i in range(start, n // k + 1):
        count += dfs(n - i, k - 1, i)
    return count


n, k = map(int, input().split())
print(dfs(n, k, start=1))
