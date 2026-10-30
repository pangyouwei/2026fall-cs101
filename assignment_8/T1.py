def hanoi(n: int, src: str, aux: str, dst: str, moves: list) -> None:
    if n == 0:
        return

    hanoi(n - 1, src, dst, aux, moves)
    moves.append(f"{n}:{src}->{dst}")
    hanoi(n - 1, aux, src, dst, moves)


num, a, b, c = input().split()
num = int(num)
lst = []
hanoi(num, a, b, c, lst)
print("\n".join(lst))
