graph = [
    [1, 1, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]
]

move = [[0,1], [0,-1], [1, 0], [-1, 0]]
visit = [[0]*7 for _ in range(7)]
visit[0][0] = 1

def bfs(x, y):
    q = [[x, y]]

    while q:
        pos = q.pop(0)
        if pos[0] == 6 and pos[1] == 6:
            break
        for i in move:
            aPos = [pos[0] + i[0], pos[1] + i[1]]
            if 0 <= aPos[0] <= 6 and 0 <= aPos[1] <= 6 and graph[aPos[0]][aPos[1]] == 1 and visit[aPos[0]][aPos[1]] == 0:
                visit[aPos[0]][aPos[1]] = visit[pos[0]][pos[1]] + 1
                print(visit[aPos[0]][aPos[1]])
                q.append(aPos)
                print(q)
    print(visit)
bfs(0,0)

