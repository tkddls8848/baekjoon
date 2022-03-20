n = int(input())
datas = []
ranks = []
for i in range(n):
    datas.append(list(map(int, input().split(" "))))
    ranks.append(1)

for d in datas:
    for i in datas:
        if d == i:
            continue
        if d[0] > i[0] and d[1] > i[1]:
            ranks[datas.index(i)] += 1

for rank in ranks:
    print(rank, end=' ')