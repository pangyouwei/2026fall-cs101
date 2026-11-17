class WeightedDSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        # 0 与父节点同类；1 被父节点吃；2 吃父节点
        self.weight = [0] * n

    def find(self, x):
        path = []
        while x != self.parent[x]:
            path.append(x)
            x = self.parent[x]
        root = x
        for node in reversed(path):
            self.weight[node] = (self.weight[node] + self.weight[self.parent[node]]) % 3
            self.parent[node] = root
        return root

    def union(self, op, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False
        req = 0 if op == 1 else 1
        if self.size[ra] < self.size[rb]:
            a, b = b, a
            ra, rb = rb, ra
            req = (-req) % 3
        self.parent[rb] = ra
        self.weight[rb] = (self.weight[a] - self.weight[b] - req) % 3
        self.size[ra] += self.size[rb]
        return True

    def connected(self, a, b):
        return self.find(a) == self.find(b)


N, K = map(int, input().split())
dsu = WeightedDSU(N)

ans = 0
for _ in range(K):
    D, X, Y = map(int, input().split())
    X -= 1
    Y -= 1
    if X >= N or Y >= N:
        ans += 1
    else:
        if D == 2 and X == Y:
            ans += 1
        else:
            if D == 1:
                is_lie = dsu.connected(X, Y) and (dsu.weight[X] - dsu.weight[Y]) % 3 != 0
            else:
                is_lie = dsu.connected(X, Y) and (dsu.weight[X] - dsu.weight[Y]) % 3 != 1

            if is_lie:
                ans += 1
            else:
                dsu.union(D, X, Y)

print(ans)
