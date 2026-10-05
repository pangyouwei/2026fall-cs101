n = int(input())
events = [int(i) for i in input().split()]

x = 0
answer = 0
for event in events:
    if event == -1 and x <= 0:
        answer += 1
    else:
        x += event

print(answer)
