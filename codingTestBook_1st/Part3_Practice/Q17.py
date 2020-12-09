'''
3 3
1 0 2
0 0 0
3 0 0
2 3 2

3 3
1 0 2
0 0 0
3 0 0
1 2 2
'''
from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
s, x, y = map(int, input().split())
visited = [[False]*n for i in range(n)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
q = deque()
starts = []


def startList(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if not graph[i][j] == 0:
                starts.append([graph[i][j], i, j])
    starts.sort(key=lambda x:x[0])


def virusMove(starts):
    time = 1
    for _ in starts:
        q.append(_)
        visited[_[1]][_[2]] = True
    while q and not time == s:
        pos = q.popleft()
        print('pos',pos)
        for _ in move:
            print(pos[1] , _[0], pos[2] , _[1])
            nx, ny = pos[1] + _[0], pos[2] + _[1]
            if 0 <= nx < n and 0 <= ny < n:
                print(n, nx, ny, visited[nx][ny])
                time += 1
                if graph[nx][ny] == 0 and not visited[nx][ny]:
                    print(pos[0])
                    graph[nx][ny] = pos[0]
                    visited[nx][ny] = False
                    q.append([pos[0], nx, ny])
    print(graph)
    print(graph[x-1][y-1])
startList(graph)
virusMove(starts)



