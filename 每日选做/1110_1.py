class WeightedDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.weight = [0] * n

    def find(self, x):
        path = []
        while self.parent[x] != x:
            path.append(x)
            x = self.parent[x]
        root = x
        for node in reversed(path):
            self.weight[node] ^= self.weight[self.parent[node]]
            self.parent[node] = root
        return root

    def union(self, op, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if op == 0:
            self.weight[rb] = self.weight[a] ^ self.weight[b] ^ 0
        else:
            self.weight[rb] = self.weight[a] ^ self.weight[b] ^ 1
        self.size[ra] += self.size[rb]
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


n, m = map(int, input().split())
dsu = WeightedDSU(n)

for _ in range(m):
    a, b, D = map(int, input().split())
    if D == 0:
        is_lie = dsu.connected(a, b) and dsu.weight[a] ^ dsu.weight[b] != 0
    else:
        is_lie = dsu.connected(a, b) and dsu.weight[a] ^ dsu.weight[b] == 0
    if is_lie:
        print("NO")
        break
    dsu.union(D, a, b)
else:
    print("YES")
