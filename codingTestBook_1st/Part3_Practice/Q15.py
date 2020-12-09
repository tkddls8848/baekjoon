'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
from collections import deque


n, m, k, x = list(map(int, input().split()))
visited = [False]*(n+1)
distance = [0]*(n+1)
graph = [[] for _ in range(m+1)]


for _ in range(m):
    a, b = list(map(int, input().split()))
    graph[a].append(b)


def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        for _ in graph[now]:
            if not visited[_]:
                visited[_] = True
                distance[_] = distance[now] + 1
                q.append(_)


bfs(k)

check = False
for i in range(1, n + 1):
    if distance[i] == x:
        check = True
        print(i, end=' ')

if not check:
    print(-1)