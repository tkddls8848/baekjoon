from collections import deque

graph = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0]
]

visited = [[False]*7 for _ in range(0,7)]
move = [[-1,0], [1,0], [0,1], [0,-1]]
group = []


def bfs(x,y):
    q = deque([[x,y]])
    cnt = 0
    if not visited[x][y] and graph[x][y] == 1:
        graph[x][y] = 0
        visited[x][y] = True
        cnt += 1
    while q:
        pos = q.popleft()
        for i in move:
            nx, ny = pos[0]+i[0], pos[1]+i[1]
            if 0 <= nx <= 6 and 0 <= ny <= 6:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    cnt += 1
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    q.append([nx, ny])

    if not cnt == 0:
        group.append(cnt)
        group.sort()
        print(group, len(group))

for i in range(0,7):
    for j in range(0,7):
        bfs(i,j)
