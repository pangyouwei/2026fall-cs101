while True:
    try:
        n = int(input())
        batteries = list(map(int, input().split()))
        maximum = max(batteries)
        total = sum(batteries)
        print(f"{min(total / 2, total - maximum):.1f}")  # 贪心！
    except EOFError:
        break
