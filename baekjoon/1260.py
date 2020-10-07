from collections import deque

graph = [
    [],
    [2,3,4],
    [1,4],
    [1,4],
    [1,2,3]
]
dVisited = [False] * 5
bVisited = [False] * 5


def dfs(graph, dVisited, node):
    dVisited[node] = True
    print(node, end=' ')
    for i in graph[node]:
        if not dVisited[i]:
            dfs(graph, dVisited, i)


dfs(graph, dVisited, 1)
print()

def bfs(graph, bVisited, node):
    q = deque([node])
    bVisited[node] = True
    while q:
        num = q.popleft()
        print(num, end=' ')
        for i in graph[num]:
            if not bVisited[i]:
                q.append(i)
                bVisited[i] = True

bfs(graph, bVisited, 1)