'''
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
'''

def find_setNum(node, num):
    if not node[num] == num:
        node[num] = find_setNum(node, node[num])
    return node[num]

def union_setNum(node, a, b):
    a = find_setNum(node, a)
    b = find_setNum(node, b)
    if a < b:
        node[b] = a
    else:
        node[a] = b

v, e = map(int, input().split())
node = []
information = []
totalCost = 0
for i in range(v+1):
    node.append(i)

for i in range(e):
    a, b, cost = map(int, input().split())
    information.append([cost, a, b])

information.sort()

for i in information:
    if not find_setNum(node, i[1]) == find_setNum(node, i[2]):
        union_setNum(node, i[1], i[2])
        totalCost += i[0]

print(totalCost)


