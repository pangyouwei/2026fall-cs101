class ExtendedDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

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
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


n, m = map(int, input().split())
dsu = ExtendedDSU(2 * n)

for _ in range(m):
    a, b, D = map(int, input().split())
    if D == 0:
        is_lie = dsu.connected(a, b + n)
    else:
        is_lie = dsu.connected(a, b)
    if is_lie:
        print("NO")
        break
    if D == 0:
        dsu.union(a, b)
        dsu.union(a + n, b + n)
    else:
        dsu.union(a, b + n)
        dsu.union(a + n, b)
else:
    print("YES")
