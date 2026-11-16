class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.count = n

    def find(self, x):
        root = x
        while root != self.parent[root]:
            root = self.parent[root]
        while self.parent[x] != x:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt
        return root

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]
        self.count -= 1
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


n, m, q = map(int, input().split())

total = n * m
TOP = total  # 虚拟顶部节点
BOTTOM = total + 1  # 虚拟底部节点
dsu = DSU(total + 2)
opened = [[False] * m for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
answer = -1

for step in range(1, q + 1):
    r, c = map(int, input().split())
    r -= 1
    c -= 1
    opened[r][c] = True
    if r == 0:
        dsu.union(r * m + c, TOP)
    if r == n - 1:
        dsu.union(r * m + c, BOTTOM)
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < m and opened[nr][nc]:
            dsu.union(r * m + c, nr * m + nc)

    if dsu.connected(TOP, BOTTOM):
        answer = step
        break

print(answer)
