n = int(input())
ini_students = list(map(int, input().split()))
students = []
for i in range(n):
    students.append((ini_students[i], i))
students.sort()

total_waiting_time = 0
order = []
for i in range(n):
    order.append(str(students[i][1] + 1))
    total_waiting_time += students[i][0] * (n - i - 1)

print(' '.join(order))
print(f"{total_waiting_time / n:.2f}")
