n = int(input())
students = list(map(int, input().split()))
initial = dict(enumerate(students, 1))
final = dict(sorted(initial.items(), key=lambda x: x[1]))

total_waiting_time = 0
k = 1
for i, student in final.items():
    total_waiting_time += student * (n - k)
    k += 1
print(*final.keys())
average_waiting_time = total_waiting_time / n
print(f"{average_waiting_time:.2f}")
