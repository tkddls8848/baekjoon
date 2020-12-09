'''
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
'''
n, m = map(int, input().split())
parent_node = [i for i in range(n+1)]
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
plan = list(map(int, input().split()))


def find_parent(parent_node, node_group):
    if not parent_node[node_group] == node_group:
        return find_parent(parent_node, parent_node[node_group])
    else:
        return node_group


def union_parent(parent_node, uni_node1, uni_node2):
    uni1, uni2 = find_parent(parent_node, uni_node1), find_parent(parent_node, uni_node2)
    parent_node[uni1], parent_node[uni2] = min(uni1, uni2), min(uni1, uni2)


for i in range(1,n):
    for j in range(1,n):
        if graph[i-1][j-1] == 1:
            union_parent(parent_node,i,j)
flag = False
for i in range(n):
    if parent_node[1:].count(i) == m:
        flag = True

if flag:
    print('YES')
else:
    print('NO')