def dfs(x: int, y: int, ch: str):
    if x < 0 or x >= n or y < 0 or y >= n:
        return
    if m[x][y] != ch or visited[x][y]:
        return
    visited[x][y] = True  # 标记已遍历过的元素（套路）
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        dfs(x + dx, y + dy, ch)


k = int(input())
for _ in range(k):
    n = int(input())
    m = [list(input()) for _ in range(n)]
    ans_1 = ans_2 = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and m[i][j] == 'r':
                ans_1 += 1
                dfs(i, j, 'r')
            if not visited[i][j] and m[i][j] == 'b':
                ans_2 += 1
                dfs(i, j, 'b')
    print(ans_1, ans_2)
