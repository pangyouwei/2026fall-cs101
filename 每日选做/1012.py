s, n = map(int, input().split())
dragons = []
for _ in range(n):
    x, y = map(int, input().split())
    dragons.append((x, y))
dragons.sort(key=lambda dragon: dragon[0])

for i in range(n):
    x_i = dragons[i][0]
    y_i = dragons[i][1]
    if s > x_i:
        s += y_i
    else:
        print("NO")
        break
else:
    print("YES")
