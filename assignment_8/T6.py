def strange_hanoi(n: int, a: str, b: str, c: str, d: str):
    if n == 0:
        return 0

    moves = []
    for k in range(1, n + 1):
        moves.append(strange_hanoi(n - k, a, d, c, b) + (2 ** k - 1) + strange_hanoi(n - k, b, a, c, d))
    return min(moves)

for i in range(1, 13):
    print(strange_hanoi(i, "A", "B", "C", "D"))
