l, n = map(int, input().split())
min_list = []
max_list = []

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    min_list.append(row[0])
    max_list.append(row[1])

all_trees = l + 1
all_subway = 0
overlap = 0

trees = all_trees - all_subway + (overlap // 2)
print(trees)
