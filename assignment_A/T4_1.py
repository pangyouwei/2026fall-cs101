class WeightedDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        # weight[x]: 'x'与“当前父节点”的关系
        self.weight = [0] * n  # 0同帮；1异帮

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

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.weight[rb] = self.weight[a] ^ self.weight[b] ^ 1
        self.size[ra] += self.size[rb]
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    dsu = WeightedDSU(N)
    for _ in range(M):
        lst = input().split()
        a, b = int(lst[1]) - 1, int(lst[2]) - 1
        if lst[0] == "D":
            dsu.union(a, b)
        else:
            if not dsu.connected(a, b):
                print("Not sure yet.")
            else:
                if dsu.weight[a] == dsu.weight[b]:
                    print("In the same gang.")
                else:
                    print("In different gangs.")
