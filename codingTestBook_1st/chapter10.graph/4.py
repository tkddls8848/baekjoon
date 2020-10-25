'''
3 3
1 2
1 3
2 3
'''

def find_setNum(node, x):
    if not node[x] == x:
        find_setNum(node, node[x])
    return node[x]

def union_setNum(node, a, b):
    if a < b:
        node[b] = a
    elif a > b:
        node[a] = b

v, e = map(int, input().split())
node = []
cycle = False
for i in range(v+1):
    node.append(i)

for i in range(1, e):
    a, b = map(int, input().split())
    union_setNum(node, find_setNum(node, a), find_setNum(node, b))
    if find_setNum(node, a) == find_setNum(node, b):
        cycle = True


print(node, cycle)
