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


case_num = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    case_num += 1

    dsu = DSU(n)
    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        dsu.union(i, j)
    ans = dsu.count

    print(f"Case {case_num}: {ans}")
