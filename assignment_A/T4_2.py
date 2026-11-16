class ExtendedDSU:
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


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dsu = ExtendedDSU(2 * N)

    for _ in range(M):
        op, x, y = input().split()
        x, y = int(x) - 1, int(y) - 1

        if op == 'D':
            dsu.union(x, y + N)
            dsu.union(x + N, y)
        else:
            if dsu.find(x) == dsu.find(y):
                print("In the same gang.")
            elif dsu.find(x) == dsu.find(y + N) or dsu.find(x + N) == dsu.find(y):
                print("In different gangs.")
            else:
                print("Not sure yet.")
