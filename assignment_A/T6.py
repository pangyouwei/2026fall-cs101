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


N, K = map(int, input().split())
dsu = ExtendedDSU(3 * N)

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
                is_lie = dsu.connected(X, Y + N) or dsu.connected(Y, X + N)
            else:
                is_lie = dsu.connected(X, Y) or dsu.connected(Y, X + N)

            if is_lie:
                ans += 1
            else:
                if D == 1:
                    dsu.union(X, Y)
                    dsu.union(X + N, Y + N)
                    dsu.union(X + 2 * N, Y + 2 * N)
                elif D == 2:
                    dsu.union(X, Y + N)
                    dsu.union(X + N, Y + 2 * N)
                    dsu.union(X + 2 * N, Y)

print(ans)
