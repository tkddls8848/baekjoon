'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
'''
from collections import deque

n, m = map(int, input().split())
graph = [[] for i in range(n)]
tmp = [[0] * m for i in range(n)]
visited = [[False] * m for i in range(n)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
q = deque()
result = 0

for i in range(m):
    graph[i] = list(map(int, input().split()))


def spread(start):
    graph[start[0]][start[1]] = 2
    visited[start[0]][start[1]] = True
    q.append(start)
    while q:
        node = q.popleft()
        for _ in move:
            nx, ny = node[0] + _[0], node[1] + _[1]
            if 0 <= nx <= 6 and 0 <= ny <= 6:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 1
                if not graph[nx][ny] == 1 and not visited[nx][ny]:
                    graph[nx][ny] = 2
                    visited[nx][ny] = True
                    q.append([nx, ny])


def score():
    cnt = 0
    for i in range(len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt


def split(count):
    global result
    if count == 3:
        for i in range(n):
            for j in range(m):
                tmp[i][j] = graph[i][j]
        for i in range(n):
            for j in range(m):
                if tmp[i][j] == 2:
                    spread([i, j])
                    print(score())
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count = count + 1
                split(count)
                graph[i][j] = 0
                count = count - 1


split(0)
