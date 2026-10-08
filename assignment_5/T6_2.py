from collections import deque
import sys

data = sys.stdin.read().strip().split()
n = int(data[0])
k = int(data[1])
events = list(map(int, data[2: n + 2]))

q = deque()
undone = 0

for t in range(n):
    if events[t] > 0:
        # 招募 events[t] 名警察，退役时间为 t + k - 1
        for _ in range(events[t]):
            q.append(t + k - 1)
    elif events[t] == -1:
        # 清除已过期的警察
        while q and q[0] < t:
            q.popleft()
        if q:
            q.popleft()  # 派出最早入伍的警察
        else:
            undone += 1  # 没有可用警察，犯罪无法处理

print(undone)
