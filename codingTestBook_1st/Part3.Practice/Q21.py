'''
2 20 50
50 30
20 40

2 40 50
50 30
20 40

3 5 10
10 15 20
20 30 25
40 22 10

3 5 10
11 16 21
0 0 0
11 16 21
'''
from collections import deque

n, lowNum, maxNum = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))
opened = [[False]*n for i in range(n)]
visited = [[False]*n for i in range(n)]
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
q = deque()


## 특정 영역에서 이동 가능 영역 탐색
def search(x, y):
    s = deque()
    s.append([x, y])
    while s:
        a, b = s.popleft()
        for _ in move:
            na, nb = a + _[0], b + _[1]
            if 0 <= na < n and 0 <= nb < n and not opened[na][nb]:
                if lowNum <= abs(graph[a][b] - graph[na][nb]) <= maxNum:
                    opened[a][b], opened[na][nb] = True, True
                    s.append([na, nb])


## 이동 가능 영역에 대한 영역 합, 수 탐색
def trueBFS(x, y):
    total, cnt = 0, 0
    search(x, y)
    area = deque()
    if opened[x][y]:
        q.append([x, y])
    while q:
        pos = q.popleft()
        for _ in move:
            nx, ny = pos[0]+_[0], pos[1]+_[1]
            if 0 <= nx < n and 0 <= ny < n:
                if opened[nx][ny] and not visited[nx][ny]:
                    total += graph[nx][ny]
                    visited[nx][ny] = True
                    q.append([nx, ny])
                    area.append([nx, ny])
                    cnt += 1
    return area


## 합, 수 나누기
def unit(queue):
    total, cnt = 0, 0
    flag = False
    while queue:
        pos = queue.popleft()
        total += graph[pos[0]][pos[1]]
        cnt += 1
        print('t',total)
    if not cnt == 0:
        unitnum = total // cnt
        flag = True
        print(total,cnt,unitnum)
        for a in range(n):
            for b in range(n):
                if opened[a][b]:
                    graph[a][b] = unitnum
                    print('unitnum', unitnum)
                    opened[a][b] = False
    return flag


while True:
    fl = False
    cnt = 0
    for i in range(n):
        for j in range(n):
            print('============')
            if unit(trueBFS(i, j)):
                fl = True
                print('before', cnt)
    cnt += 1
    print('aft', cnt)
    if not fl:
        print(cnt)
        break







