n = int(input())
solvable_problems = 0

for i in range(n):
    a, b, c = map(int, input().split())
    if a + b + c >= 2:
        solvable_problems += 1

print(solvable_problems)
