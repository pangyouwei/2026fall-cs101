n = int(input())
goods = list(map(int, input().split()))
goods.sort(reverse=True)

ans = sum(goods)
for i in range(n % 3):
    goods.pop(-1)
for i in range(2, len(goods), 3):
    ans -= goods[i]

print(ans)
