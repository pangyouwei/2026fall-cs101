n = int(input())
coins = [int(x) for x in input().split()]
coins.sort(reverse=True)

mine = 0
his = sum(coins)
ans = 0

while mine <= his:
    mine += coins[ans]
    his -= coins[ans]
    ans += 1
print(ans)
