n, k = map(int, input().split())
events = list(map(int, input().split()))

q = []
head = 0
undone = 0

for t in range(n):
    if events[t] > 0:
        for _ in range(events[t]):
            q.append(t + k - 1)
    elif events[t] == -1:
        # 清除过期警察
        while head < len(q) and q[head] < t:
            head += 1
        if head < len(q):
            head += 1  # 派出最早入伍的警察
        else:
            undone += 1

print(undone)
