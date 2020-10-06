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
visited = [False] * 8


def bfs(node):
    q = deque()
    for n in graph[node]:
        q.append(n)
    while q:
        curCom = q.popleft()
        visited[node] = True
        if not visited[curCom]:
            for i in graph[curCom]:
                q.append(i)
                visited[curCom] = True


bfs(2)


count = 0
for v in visited:
    if v:
        count += 1
print(count)