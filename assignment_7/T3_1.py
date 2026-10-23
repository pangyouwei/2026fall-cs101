from collections import deque

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    lst = [_ for _ in range(1, n + 1)]
    monkeys = deque(lst)
    i = 0
    while i < n - 1:
        monkeys.rotate(n - i - m + 1)
        monkeys.popleft()
        i += 1

    print(monkeys[0])
