n = int(input())
costumers = list(map(int, input().split()))

five = 0
ten = 0

for i in range(n):
    if costumers[i] == 5:
        five += 1
    elif costumers[i] == 10:
        if five:
            five -= 1
            ten += 1
        else:
            print("NO")
            break
    else:
        if ten > 0 and five > 0:
            ten -= 1
            five -= 1
        elif ten == 0 and five >= 3:
            five -= 3
        else:
            print("NO")
            break
else:
    print("YES")
