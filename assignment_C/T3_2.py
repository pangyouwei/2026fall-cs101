# bfs
from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i * i for i in range(1, int(n ** 0.5) + 1)][::-1]  # 倒序可提速
        ps_set = set(ps)
        queue = deque([n])
        hashtable = {n: 1}

        while queue:
            val = queue.popleft()
            if val in ps_set:
                return hashtable[val]
            for p in ps:
                if val > p and val - p not in hashtable:
                    queue.append(val - p)
                    hashtable[val - p] = hashtable[val] + 1

        return -1
