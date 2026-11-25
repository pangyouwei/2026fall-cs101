from functools import lru_cache


@lru_cache(maxsize=None)
def dfs(n: int, k: int) -> int:
    if n < k:
        return 0
    if k == 1:
        return 1
    return dfs(n - 1, k - 1) + dfs(n - k, k)


n, k = map(int, input().split())
print(dfs(n, k))
