mode = int(input())

if mode == 1:
    x = int(input())
    print(abs(x))
if mode == 2:
    a, b, c = map(int, input().split())
    print(a + b, b + c, c + a)
if mode == 3:
    a, b, c = map(int, input().split())
    print(a + b)
    print(b + c)
    print(c + a)
if mode == 4:
    print("->".join(input().split()))
if mode == 5:
    n = int(input())
    nums = map(int, input().split())
    for num in nums:
        print(f"{num}#", end='')
if mode == 6:
    n = int(input())
    nums = sorted(map(int, input().split()), reverse=True)
    for num in nums:
        print(num, end=' ')
if mode == 7:
    a, b = map(int, input().split())
    print(f"{a}*{b}={a * b}")
if mode == 8:
    a, b = map(int, input().split())
    answer = a / b
    print(f"{answer:.3f}")
if mode == 9:
    n = int(input())
    nums = input().split()
    print(",".join(nums))
