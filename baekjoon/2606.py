from collections import deque

graph =[
    [],
    [2,5],
    [1,3,5],
    [2],
    [7],
    [1,2,6],
    [5],
    [4]
]
bVisited = [False] * 8
dVisited = [False] * 8

def bfs(node):
    q = deque()
    for n in graph[node]:
        q.append(n)
    while q:
        curCom = q.popleft()
        bVisited[node] = True
        if not bVisited[curCom]:
            for i in graph[curCom]:
                q.append(i)
                bVisited[curCom] = True
bfs(1)

count = 0
for v in bVisited:
    if v:
        count += 1
print(count)

def dfs(node):
    for i in graph[node]:
        if not dVisited[i]:
            dVisited[i] = True
            dfs(i)

dfs(7)
dCount = 0
for v in dVisited:
    if v:
        dCount += 1
print(dCount)
